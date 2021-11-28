## Program Goals
## 1 Get tickets list using requests if error with connection print out error code
## 2 Display tickets with string formater
## 3 Allow user to pick out a certain ticket by imputting ticket Number in CLIimport requests
from TicketViewer import TicketViewer

## Below is user credentials
## To test with different cridentials replace zcccountryfinancial with own subdomain, replace user with own email address, replace pwd with own password
url = "https://zcccountryfinancial.zendesk.com/api/v2/tickets.json"
user = "jtj4@illinois.edu"
pwd = "Chockey121#121"
application = TicketViewer()
application._init_(url, user, pwd)
application.connecttozendeskapi()
application.runapplication()
