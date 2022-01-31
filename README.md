# O365_email
A functional demo of the O365 Module to send an email on an authenticated, tokenized account.

## Prep
* Create an app in Azure Developer's portal (*to do* create visual steps)
* Create Secret, and copy tennant, client and secret (*to do* create visual steps)
* Load the python script, with dotenv, O365

## Usage
* Can be imported or copied into your own scripts
* Usage is email(emailto, emailsubject, emailbody, emailfrom='emailaddress@senderandappauthor.com', emailcc=None)
_  * Where **emailto** is your intended recipient
  * **emailsubject** is the email subject
  * **emailbody** is the body of the email
  * **emailfrom** is the email that it's being sent from.  Note that this account must be authorized.
  * **emailcc** is the CC email address_
* On first usage, the script will give you a URL to paste into a browser.  It will change the URL, and you must copy this back into the script for it to work.  You will get a success message.<br>
![unnamed](https://user-images.githubusercontent.com/76273795/151882231-3aa44b35-cce0-4ec7-b709-881d79339437.png)<br>


## Credits
This is a demonstration of the usage of Microsoft Graph API, as set: https://github.com/O365/python-o365 <br>
Super big thanks to https://github.com/jrmatchett for reviewing my code and help refactor it!<br>

## License
[MIT](https://choosealicense.com/licenses/mit/)
