import requests


class TicketViewer:
    data = []
    url = ""
    user = ""
    pwd = ""

    def _init_(self, userurl, useremail, userpwd):
        self.url = userurl
        self.user = useremail
        self.pwd = userpwd

    def connecttozendeskapi(self):
        response = requests.get(self.url, auth=(self.user, self.pwd))
        if response.status_code != 200:
            print("Status:", response.status_code, "Problem with the request. Exiting.")
            exit()
        self.data = response.json()

    def printalltickets(self):
        for ticket in self.data["tickets"]:
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

    def printspecificticket(self, tickenumber):
        for ticket in self.data["tickets"]:
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

    def runapplication(self):

        while exit != True:
            value = input(
                "Hello! Please input 1 to view all the tickets,2 to view a specific ticket or 3 to quit the program "
            )
            v1 = int(value)
            if v1 == 1:
                self.printalltickets()
            if v1 == 2:
                ticketnumber = input("Please enter ticket ID number to view ")
                self.printspecificticket(ticketnumber)
            if v1 == 3:
                quit()
