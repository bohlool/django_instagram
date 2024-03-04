from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class AccountTests(APITestCase):

    def setUp(self):
        self.user_data = {'username': 'liana', 'password': 'pass1234', 'first_name': 'Liana', 'last_name': 'Mohammadi'}

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('register-list')

        response = self.client.post(url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 4)

    def test_login(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('token_obtain_pair')

        User.objects.create_user(**self.user_data)
        response = self.client.post(url,
                                    {'username': self.user_data['username'], 'password': self.user_data['password']},
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_change_password(self):
        """
        Ensure we can create a new account object.
        """
        user = User.objects.create_user(**self.user_data)

        self.client.force_authenticate(user=user)

        url = reverse('change-pass-detail', args=[user.id])
        new_password = 'p1234567'
        response = self.client.put(url,
                                   {'password': new_password, 'confirm_password': new_password},
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_change_account(self):
        """
        Ensure we can create a new account object.
        """
        user = User.objects.create_user(**self.user_data)
        self.client.force_authenticate(user=user)

        url = reverse('change-account-detail', args=[user.id])
        new_username = 'farnaz'
        response = self.client.put(url,
                                   {'username': new_username},
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
        new_user = User.objects.get(pk=user.id)
        self.assertEqual(new_user.username, new_username)

    def test_delete_account(self):
        """
        Ensure we can create a new account object.
        """
        user = User.objects.create_user(**self.user_data)

        self.client.force_authenticate(user=user)

        url = reverse('change-account-detail', args=[user.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)
