from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.urls.base import reverse

class PizzaLoginTest(TestCase):
    def setUp(self):
        User.objects.create_user("demo_1", "test@test.com", "t3stp4ssw0rd!")

    def test_login_success(self):
        c = Client()
        response = c.post(reverse('proxy_auth'),
                          data={'form-username': 'demo_1',
                                'form-password': 't3stp4ssw0rd!',
                                'next_page': 'home_page'},
                          follow=True)

        success_page = '/vote_manager/home_page/'
        result_page = response.redirect_chain[0][0]

        # if logged in, client is redirected to home
        self.assertEqual(success_page, result_page)

    def test_login_failure(self):
        c = Client()
        response = c.post(reverse('proxy_auth'),
                          data={'form-username': 'demo_1',
                                'form-password': 'wr0ngp4ssw0rd!',
                                'next_page': 'home_page'},
                          follow=True)

        failure_page = '/auth_voters/login/'
        result_page = response.redirect_chain[0][0]

        # if not logged in, client is redirected to login page
        self.assertEqual(failure_page, result_page)

    def test_logout(self):
        c = Client()

        response = c.get(reverse('logout'), follow=True)

        success_page = '/auth_voters/login?next=/auth_voters/logout/'
        result_page = response.redirect_chain[0][0]

        # if logged out, is redirected to login with ?next= 
        self.assertEqual(success_page, result_page)
