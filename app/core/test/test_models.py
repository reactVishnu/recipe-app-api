'''
Test for models
'''
from django.test import TestCase
from django.contrib.auth import get_user_model
from decimal import Decimal
from core import models


class Modeltests(TestCase):
    def test_create_user_with_email_successful(self):
        email = 'test@example.com'
        password = 'testpass123'

        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        '''Test email is normalized for new user'''
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', "sample123")

    def test_create_recepie(self):
        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpass123'
        )

        recipe = models.Recipe.objects.create(
            user=user,
            title='Sample Reciepe Name',
            time_minutes=5,
            price=Decimal('5.50'),
            description='Sample Race Description'

        )
        self.assertEqual(str(recipe), recipe.title)

    def test_create_tag(self):
        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpass123'
        )
        tag = models.Tag.objects.create(user=user, name='Tag1')

        self.assertEqual(str(tag), tag.name)

    def test_create_ingredients(self):
        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpass123'
        )
        ingredient = models.Ingredient.objects.create(
            user=user,
            name='Ingredient 1'
        )
        self.assertEqual(str(ingredient), ingredient.name)
