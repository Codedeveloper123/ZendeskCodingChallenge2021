import unittest

from requests.models import Response
from TicketViewer import TicketViewer
import pytest


class TestTicketViewerMethods(unittest.TestCase):
    ## This tests if the function returns 0 as the only way the function returns 0 is if the program goes into the if statment that prints out the htttp error code.
    def test_wrongauthentication(self):
        url = "https://zcccountryfinancial.zendesk.com/api/v2/tickets.json"
        user = "jtj5@illinois.edu"
        pwd = "Chockey121#121"
        application = TicketViewer()
        application._init_(url, user, pwd)
        self.assertEqual(0, application.connecttozendeskapi())

    ## This tests if printing all tickets are displayed with the correct amount of tickets in the ticket file
    def test_allTicketsaredisplayed(self):
        url = "https://zcccountryfinancial.zendesk.com/api/v2/tickets.json"
        user = "jtj4@illinois.edu"
        pwd = "Chockey121#121"
        application = TicketViewer()
        application._init_(url, user, pwd)
        application.connecttozendeskapi()
        self.assertEqual(27, application.printalltickets())
