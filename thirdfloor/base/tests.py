import time

import warnings
from django.core.cache import cache
from django.test.testcases import TestCase


class BaseTestCase(TestCase):

    TEST_WARN_MS = 50

    def setUp(self) -> None:
        super().setUp()
        cache.clear()
        self.test_start = time.perf_counter()

    def tearDown(self) -> None:
        duration = (time.perf_counter() - self.test_start) * 1000
        if duration > self.TEST_WARN_MS:
            warnings.warn(
                '{} is slower than {}ms: {}ms'.format(self._testMethodName, self.TEST_WARN_MS, duration),
                RuntimeWarning)
        super().tearDown()
