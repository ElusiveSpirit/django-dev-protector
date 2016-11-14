import json
import os

from django.test import TestCase, Client
from django.conf import settings

import django_dev_protector.settings
from .settings import PROTECT_STATUS_VARIABLE
from django_dev_protector.setup import get_status


class MiddlewareTests(TestCase):

    def test_block_the_server(self):
        """
        Blocks server by request
        """
        response = self.client.post('/django_dev_protector/', json.dumps({
            'key': settings.SECRET_KEY,
            'status': True
        }), content_type='application/json')
        self.assertEqual(get_status(), 'True')

    def test_is_server_blocked(self):
        response = self.client.post('/django_dev_protector/', json.dumps({
            'key': settings.SECRET_KEY,
            'status': True
        }), content_type='application/json')
        response = self.client.get('/')
        self.assertEqual(get_status(), 'True')
        self.assertContains(response, 'The work was not paid.')

    def test_unblock_the_server(self):
        """
        Unblocks server by request
        """
        response = self.client.post('/django_dev_protector/', json.dumps({
            'key': settings.SECRET_KEY,
            'status': False
        }), content_type='application/json')
        self.assertEqual(get_status(), 'False')
        self.assertEqual(os.environ[PROTECT_STATUS_VARIABLE], 'False')

    def test_is_server_unblocked(self):
        response = self.client.post('/django_dev_protector/', json.dumps({
            'key': settings.SECRET_KEY,
            'status': False
        }), content_type='application/json')
        response = self.client.get('/')
        self.assertEqual(get_status(), 'False')
        self.assertContains(response, 'works!')
