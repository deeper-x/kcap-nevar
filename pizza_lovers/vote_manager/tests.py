from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.urls.base import reverse


class PizzaVoteTest(TestCase):
    def setUp(self):
        User.objects.create_user("demo_1", "test@test.com", "t3stp4ssw0rd!")

    def test_A_vote_success(self):
        c = Client()
        c.post(reverse('proxy_auth'),
               data={'form-username': 'demo_1',
                     'form-password': 't3stp4ssw0rd!',
                     'next_page': 'home_page'},
               follow=True)

        response = c.get(reverse('send_vote'), follow=True)

        success_url = "/vote_manager/send_vote/"
        response_url = response.request['PATH_INFO']

        # registered user can access to view
        self.assertEqual(success_url,response_url)

    def test_B_vote_failure(self):
        c = Client()
        c.post(reverse('proxy_auth'),
               data={'form-username': 'demo_1',
                     'form-password': 'wr0ngp4ssw0rd!',
                     'next_page': 'home_page'},
               follow=True)

        response = c.get(reverse('send_vote'), follow=True)

        failure_url = "/auth_voters/login/"
        response_url = response.request['PATH_INFO']

        # unrecognized/anonymous user is redirected to login
        self.assertEqual(failure_url, response_url)