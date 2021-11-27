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
print(data)
