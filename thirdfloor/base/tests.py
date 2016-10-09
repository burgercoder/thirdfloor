import time
from typing import List, Any, Tuple

import warnings

from django.core.cache import cache
from django.core.management import call_command
from django.db.backends.base.base import BaseDatabaseWrapper
from django.test.runner import DiscoverRunner
from django.test.testcases import TestCase


class TestRunner(DiscoverRunner):

    def setup_databases(self, **kwargs: Any) -> List[Tuple[BaseDatabaseWrapper, str, bool]]:
        configs = super().setup_databases(**kwargs)
        call_command('datacreator')
        return configs


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
