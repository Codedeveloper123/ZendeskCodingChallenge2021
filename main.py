## Program Goals
## 1 Get tickets list using requests if error with connection print out error code
## 2 Display tickets with string formater
## 3 Allow user to pick out a certain ticket by imputting ticket Number in CLI
import requests

## Below is user credentials
url = "https://zcccountryfinancial.zendesk.com/api/v2/tickets.json"
user = "jtj4@illinois.edu"
pwd = "Chockey121#121"
## Gets data from Zendesk API
response = requests.get(url, auth=(user, pwd))
## If Zendesk API cannot connect prints out the error message
if response.status_code != 200:
    print("Status:", response.status_code, "Problem with the request. Exiting.")
    exit()
## Makes the Json into python dictionary
data = response.json()
exit = False
while exit != True:
    value = input(
        "Hello! Please input 1 to view all the tickets or 2 to view a specific ticket"
    )
    v1 = int(value)
    if v1 == 1:
        print("Function to display all tickets")
    if v1 == 2:
        ticketnumber = input("Please enter ticket number to view")

        if ticketnumber == 3:
            print("Here is ticket 3")
