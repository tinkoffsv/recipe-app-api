from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        # test user creating
        email = 'test@aaa.com'
        password = 'testPass123'
        user = get_user_model().objects.create_user(
            email=email, password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_super_u(self):
        user = get_user_model().objects.create_superuser('tt@te.com', 'tst123')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
