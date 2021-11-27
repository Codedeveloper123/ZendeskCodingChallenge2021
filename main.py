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


def printalltickets():
    for ticket in data["tickets"]:
        print(
            "Ticket with subject "
            + ticket["subject"]
            + " created at "
            + ticket["created_at"]
            + " with a priority of "
            + ticket["priority"]
            + " with an Id number "
            + str(ticket["id"])
        )


def printspecificticket(tickenumber):
    for ticket in data["tickets"]:
        if str(ticket["id"]) == tickenumber:
            print(
                "Ticket with subject "
                + ticket["subject"]
                + " created at "
                + ticket["created_at"]
                + " with a priority of "
                + ticket["priority"]
                + " with an Id number "
                + str(ticket["id"])
            )


while exit != True:
    value = input(
        "Hello! Please input 1 to view all the tickets,2 to view a specific ticket or 3 to quit the program "
    )
    v1 = int(value)
    if v1 == 1:
        printalltickets()
    if v1 == 2:
        ticketnumber = input("Please enter ticket ID number to view ")
        printspecificticket(ticketnumber)
    if v1 == 3:
        quit()
