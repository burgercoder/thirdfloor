from django.test import TestCase  # type: ignore


class SimpleTest(TestCase):

    def test_one_plus_one(self) -> None:
        self.assertEqual(2, 1+1)
