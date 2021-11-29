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

    def connect_to_zendesk_api(self):
        response = requests.get(self.url, auth=(self.user, self.pwd))
        if response.status_code != 200:
            print("Status:", response.status_code, "Problem with the request. Exiting.")
            ## Following return is for testing purposes as it is hard to test print statments
            return 0
        self.data = response.json()

    def print_all_tickets(self):
        count = 0
        count2 = 25
        exit = False
        for ticket in self.data["tickets"]:
            if count < 25:
                print(
                    "Ticket with subject "
                    + ticket["subject"]
                    + " created at "
                    + ticket["created_at"]
                    + " with an Id number "
                    + str(ticket["id"])
                )
            count = count + 1
        while exit == False:
            value = input("Press 4 to page to the next set of 25 tickets ")
            v1 = int(value)
            if v1 == 4:
                count3 = count2 + 25
                while count2 < count and count2 < count3:
                    print(
                        "Ticket with subject "
                        + self.data["tickets"][count2]["subject"]
                        + " created at "
                        + self.data["tickets"][count2]["created_at"]
                        + " with an Id number "
                        + str(self.data["tickets"][count2]["id"])
                    )
                    count2 = count2 + 1
                if count2 == count:
                    exit = True
        ## Used for testing purposes returns number of tickets displayed
        return count

    def print_specific_ticket(self, ticket_id_number):
        for ticket in self.data["tickets"]:
            if str(ticket["id"]) == ticket_id_number:
                print(
                    "Ticket with subject "
                    + ticket["subject"]
                    + " created at "
                    + ticket["created_at"]
                    + " with an Id number "
                    + str(ticket["id"])
                )
                return 0

    def run_application(self):

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
