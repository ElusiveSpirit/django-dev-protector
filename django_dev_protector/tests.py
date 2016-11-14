from django.test import TestCase, Client

import django_dev_protector.settings
from django_dev_protector.setup import get_hash, get_status, save_status


class MiddlewareTests(TestCase):

    def test_block_the_server(self):
        """
        Blocks server by request
        """
        response = self.client.get('/django_dev_protector/%s/on/' % get_hash())
        self.assertEqual(get_status(), 'True')

    def test_unblock_the_server(self):
        """
        Unblocks server by request
        """
        response = self.client.get('/django_dev_protector/%s/off/' % get_hash())
        self.assertEqual(get_status(), 'False')
