from django.test import TestCase


class SimpleTest(TestCase):

    def testOnePlusOne(self):
        self.assertEqual(2, 1+1)
