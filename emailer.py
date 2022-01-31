from dotenv import load_dotenv
from O365 import Account
from O365 import FileSystemTokenBackend
import os


def email(emailto, emailsubject, emailbody, emailfrom='emailaddress@senderandappauthor.com', emailcc=None):
    load_dotenv('C:\\pathtoenvfile\\.env')  # Change addressing to where you've stored your .env file

    scopes = ['basic', 'message_all', 'message_send', 'offline_access']  #These have also been set in the delegated access

    credentials = (os.getenv('MS_CLIENTID'), os.getenv('MS_SECRET')) #the os.getenv call is to parameters specified in your .env file

    token_backend = FileSystemTokenBackend(token_filename='C:\\pathtotokenfile\\o365_token.txt') # Change addressing to where you want your token sitting
    # Note - You want to make certain you have protected unauthorized access to this token file!

    account = Account(credentials, token_backend=token_backend, tenant_id=os.getenv('MS_TENNANTID'), scopes=scopes)

    if not account.is_authenticated:
        account.authenticate()

    mailbox = account.mailbox(emailfrom)

    m = mailbox.new_message()

    m.to.add(emailto)

    m.cc.add(emailcc)

    m.subject = emailsubject

    m.body = emailbody

    m.send()

# Used to test functionality
email(emailto='senderemail@address.com', emailsubject='Your Subject', emailbody='Your email body.')
