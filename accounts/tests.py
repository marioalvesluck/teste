from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class LoginTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')

    def test_login(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'secret'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
