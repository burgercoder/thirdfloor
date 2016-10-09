from typing import Any, Optional

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, username: str, password: str, **extra_fields: Any) -> 'User':
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username: str, password: str, **extra_fields: Any) -> 'User':
        extra_fields['is_staff'] = True
        return self.create_user(username, password, **extra_fields)


class User(AbstractBaseUser):

    username = models.CharField(max_length=30, unique=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    manager = UserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        # pylint: disable=too-few-public-methods
        db_table = 'user'

    def get_full_name(self) -> str:
        return self.username

    def get_short_name(self) -> str:
        return self.username

    def has_perm(self, perm: str, obj: Optional[models.Model]=None) -> bool:
        # pylint: disable=unused-argument
        return self.is_staff

    def has_module_perms(self, app_label: str) -> bool:
        # pylint: disable=unused-argument
        return self.is_staff

    def __str__(self) -> str:
        return self.username
