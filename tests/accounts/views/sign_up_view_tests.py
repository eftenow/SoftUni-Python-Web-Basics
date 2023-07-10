from django.test import TestCase
from django.urls import reverse


class SignUpViewTests(TestCase):
    VALID_USER_DATA = {
        'email': 'test123@abv.bg',
        'username': 'test123',
        'password1': '123QWEasd',
        'password2': '123QWEasd',
    }

    def test_sign_up__when_valid_data_expect__logged_in_user(self):
        response = self.client.post(
            reverse('register account'),
            data=self.VALID_USER_DATA
        )

        self.assertEqual(response.wsgi_request.user.username, self.VALID_USER_DATA['username'])
        self.assertEqual(response.wsgi_request.user.email, self.VALID_USER_DATA['email'])
