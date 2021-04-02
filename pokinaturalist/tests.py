from django.test import TestCase, Client
from django.core import exceptions
from django.http import HttpRequest

from . import views
from ipware import get_client_ip

class PokinaturalistAppTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        del self.client
        return super().tearDown()

    def test_for_valid_ip_addr(self):
        request = HttpRequest()
        request.META = {'HTTP_X_FORWARDED_FOR': '177.139.233.139, 198.84.193.157, 198.84.193.158'}  # From ipware library
        views_ip_addr = views.get_user_ip_addr(request)
        self.assertEqual('177.139.233.139', views_ip_addr)

    def test_index_page_returns_200(self):
        response = self.client.get("/pokinaturalist/")
        self.assertEqual(200, response.status_code)

    def test_ip_addr_stored_in_session(self):
        response = self.client.get("/pokinaturalist/")
        self.assertEqual('127.0.0.1', self.client.session.get("IPv4_ADDR"))

    def test_for_empty_ip_addr(self):
        request = HttpRequest()
        request.META = {}
        self.assertIsNone(views.get_user_ip_addr(request))