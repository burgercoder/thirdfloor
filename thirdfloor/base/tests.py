from django.test import TestCase  # type: ignore


class SimpleTest(TestCase):

    def testOnePlusOne(self) -> None:
        self.assertEqual(2, 1+1)
