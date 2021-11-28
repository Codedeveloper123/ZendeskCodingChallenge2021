import unittest
from TicketViewer import TicketViewer


class TestStringMethods(unittest.TestCase):
    def test_wrongauthentication(self):
        url = "https://zcccountryfinancial.zendesk.com/api/v2/tickets.json"
        user = "jtj5@illinois.edu"
        pwd = "Chockey121#121"
        application = TicketViewer()
        application._init_(url, user, pwd)
        self.assertEquals(
            "Status: 401 Problem with the request. Exiting.",
            application.connecttozendeskapi(),
        )

    def test_allTicketsaredisplayed(self):
        url = "https://zcccountryfinancial.zendesk.com/api/v2/tickets.json"
        user = "jtj4@illinois.edu"
        pwd = "Chockey121#121"
        application = TicketViewer()
        application._init_(url, user, pwd)
