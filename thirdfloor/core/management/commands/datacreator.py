import time
from typing import Callable, Any

from django.core.management.base import BaseCommand

from thirdfloor.account.models import User


def timed(func: Callable) -> Callable:
    def inner(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print('\t{} - {:.3f}s'.format(func.__name__, time.perf_counter()-start))
        return result
    return inner


class Command(BaseCommand):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.user = None

    @timed
    def create_users(self) -> None:
        def create_user(username: str, **kwargs: Any) -> User:
            user = User(username=username, **kwargs)
            user.set_password('password')
            user.save()
            return user
        self.user = create_user('testuser')
        create_user('staffuser', is_staff=True)

    def handle(self, *args: Any, **options: Any) -> None:
        print('-' * 70)
        print('datacreator.py started')
        start = time.time()

        self.create_users()

        end = time.time()
        print('datacreator.py finished in {:.3f}s'.format(end-start))
        print('-' * 70)
