import datetime

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import *


# Create your tests here.

def create_user_test(first_name, last_name, username, email, password):
    return CustomUser.objects.create_user(username=username, email=email, password=password ,first_name=first_name, last_name=last_name)


class ExpensesTest(TestCase):

    def test_proper_field_entries_test(self):
        user_test = CustomUser.objects.create(username='jimmy123', email='example@gmail.com', password='123', first_name='jimmy', last_name='lee')
        Expenses(user=user_test, title='Test Title', description='Testing Desc', amount='123.45')
        # Attempt to retrieve the created user from the database with a get request
        expense = self.client.get(reverse('ExpenseManagement:'))
        # Checks to see that retrieval of a user from the database successfully returns a user
        self.assertEqual(response.status_code, 200)
