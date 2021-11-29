import unittest
from requests.models import Response
from TicketViewer import TicketViewer


class TestTicketViewerMethods(unittest.TestCase):
    ## This tests if the function returns 0 as the only way the function returns 0 is if the program goes into the if statment that prints out the htttp error code.
    def test_wrong_authentication(self):
        url = "https://zcccountryfinancial.zendesk.com/api/v2/tickets.json"
        user = "jtj5@illinois.edu"
        pwd = "Chockey121#121"
        application = TicketViewer()
        application._init_(url, user, pwd)
        self.assertEqual(0, application.connect_to_zendesk_api())

    ## This tests if printing all tickets are displayed with the correct amount of tickets in the ticket file
    def test_all_tickets_are_displayed(self):
        url = "https://zcccountryfinancial.zendesk.com/api/v2/tickets.json"
        user = "jtj4@illinois.edu"
        pwd = "Chockey121#121"
        application = TicketViewer()
        application._init_(url, user, pwd)
        application.connect_to_zendesk_api()
        self.assertEqual(27, application.print_all_tickets())

    ## Tests that it goes into the if statment becuase the only way the function returns 0 is if it displays the correct ticket based on the ID number.
    def test_get_specific_ticket(self):
        url = "https://zcccountryfinancial.zendesk.com/api/v2/tickets.json"
        user = "jtj4@illinois.edu"
        pwd = "Chockey121#121"
        application = TicketViewer()
        application._init_(url, user, pwd)
        application.connect_to_zendesk_api()
        self.assertEqual(0, application.print_specific_ticket("23"))
