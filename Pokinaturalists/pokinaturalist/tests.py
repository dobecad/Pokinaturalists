from django.test import TestCase
from django.core import exceptions
from django.http import HttpRequest, HttpResponse

from . import views
from ipware import get_client_ip

class PokinaturalistAppTestCase(TestCase):
    def test_for_valid_ip_addr(self):
        request = HttpRequest()
        request.META = {'HTTP_X_FORWARDED_FOR': '177.139.233.139, 198.84.193.157, 198.84.193.158'}  # From ipware library
        views_ip_addr = views.get_user_ip_addr(request)
        self.assertEqual('177.139.233.139', views_ip_addr)

    def test_for_empty_ip_addr(self):
        request = HttpRequest()
        request.META = {}
        self.assertIsNone(views.get_user_ip_addr(request))