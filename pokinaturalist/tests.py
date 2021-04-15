from django.test import TestCase, Client
from django.core import exceptions
from django.http import HttpRequest
from django.urls import reverse

from . import views
from ipware import get_client_ip
import os

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

    def test_for_mapbox_token(self):
        self.assertIsNotNone(os.getenv('MapboxAppToken'))

    def test_view_returns_200(self):
        response = self.client.get(reverse('pokinaturalist'))
        self.assertEqual(response.status_code, 200)

    def test_mapbox_exists_in_context(self):
        response = self.client.get(reverse('pokinaturalist'))
        self.assertIsNotNone(response.context['mapboxAppToken'])

    def test_correct_base_html_is_returned(self):
        '''
        Check that the route "pokinaturalist/" returns both the base.html and the game/geo.html
        '''
        response = self.client.get('/pokinaturalist/')
        self.assertTemplateUsed(response, 'pokinaturalist/base.html', 'pokinaturalist/game/geo.html')

    def test_allowed_hosts(self):
        response = self.client.get('/pokinaturalist/', HTTP_HOST='this.is.a.test:8000')
        self.assertEqual(response.status_code, 400)

        response = self.client.get('/pokinaturalist/', HTTP_HOST='127.0.0.1')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/pokinaturalist/', HTTP_HOST='pokinaturalists.herokuapp.com')
        self.assertEqual(response.status_code, 200)

    def test_geo_html(self):
        response = self.client.get('/pokinaturalist/')
        self.assertContains(response, '<div id="parent" class="container-md">')
        self.assertContains(response, '<div id="map')
