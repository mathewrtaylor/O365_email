"""
Sends an email via the Microsoft Graph API using a authenticated O365 account.

This script authenticates to the Microsoft Graph API using application credentials 
configured in Azure Active Directory. It then uses the O365 Python library to 
construct and send an email from the authenticated account.

The email parameters (recipient, subject, body, etc.) are passed as arguments 
to the email() function. The credentials are read from environment variables 
that should be set up as part of configuration.

Usage:
    python send_email.py

Author: Mathew Taylor
License: MIT
"""
import os
from dotenv import load_dotenv
from O365 import Account
from O365 import FileSystemTokenBackend
from pathlib import Path


def email(emailto, emailsubject, emailbody, emailfrom='emailaddress@senderandappauthor.com', emailcc=None):
    """
    Composes and sends an email via the Microsoft Graph API.
    
    Parameters:
        emailto (str): Recipient email address.
        emailsubject (str): Subject line of the email.
        emailbody (str): Body text of the email.
        emailfrom (str): Sender email address.
        emailcc (str): CC email address.
        
    Returns:
        None: The email is sent via the API.
        
    """
    load_dotenv(Path.home() / "Documents/GitHub" / ".env")  # Change addressing to where you've stored your .env file
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

if __name__ == "__main__":
    # Used to test functionality
    email(emailto='senderemail@address.com', emailsubject='Your Subject', emailbody='Your email body.')
