"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from controltrans.core.utils import *


class UtilsTest(TestCase):
    def test_parse_fornecedor(self):
        soup = read_xml('39869.xml')
        fornecedor = parse_fornecedor(soup)
        self.assertEqual(fornecedor.cnpj, soup.emit.cnpj.text)

    def test_parse_client(self):
        soup = read_xml('39869.xml')
        client = parse_client(soup)
        self.assertEqual(client.cnpj, soup.dest.cnpj.text)

    def test_verify_carrier_true(self):
        soup = read_xml('39869.xml')
        self.assertTrue(verify_carrier(soup))
