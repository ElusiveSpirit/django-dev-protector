import json
from django.test import TestCase, Client
from django.conf import settings

import django_dev_protector.settings
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

    def test_unblock_the_server(self):
        """
        Unblocks server by request
        """
        response = self.client.post('/django_dev_protector/', json.dumps({
            'key': settings.SECRET_KEY,
            'status': False
        }), content_type='application/json')
        self.assertEqual(get_status(), 'False')
