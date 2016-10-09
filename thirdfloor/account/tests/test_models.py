from thirdfloor.account.models import User
from thirdfloor.base.tests import BaseTestCase


class UserManagerTest(BaseTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.manager = User.manager

    def test_create_user(self) -> None:
        user = self.manager.create_user('exampleuser', 'password')
        self.assertTrue(user.check_password('password'))
        self.assertFalse(user.is_staff)

    def test_create_superuser(self) -> None:
        user = self.manager.create_superuser('exampleuser', 'password')
        self.assertTrue(user.check_password('password'))
        self.assertTrue(user.is_staff)
