from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from petstagram.pets.models import Pet
from petstagram.photos.models import Photo

UserModel = get_user_model()


def create_pets(user, count=5):
    return [Pet(
        name=f'pet{i}',
        personal_photo=f'https://photoasdasd.com/{i}.jpg',
        user=user
    ).save() for i in range(count)]


def create_photos(user, count=5):
    return [Photo(
        photo=f'photo{i}',
        user=user
    ).save() for i in range(count)]

class AccountDetailsView(TestCase):
    VALID_USER_DATA = {
        'email': 'test123@abv.bg',
        'username': 'test123',
        'password': '123QWEasd'
    }

    def create_user_and_login(self, user_data):
        user = UserModel.objects.create_user(**user_data)
        self.client.login(**user_data)
        return user

    def test_details__when_user_is_owner__expect_true(self):
        user = self.create_user_and_login(self.VALID_USER_DATA)
        response = self.client.get(reverse('account details', kwargs={'pk': user.pk}))

        self.assertTrue(response.context['is_owner'])

    def test_details__when_user_is_owner__expect_false(self):
        user = self.create_user_and_login(self.VALID_USER_DATA)
        self.create_user_and_login({
            'email': 'user2@abv.bg',
            'username': 'user2',
            'password': '123QWEasd'
        })
        response = self.client.get(reverse('account details', kwargs={'pk': user.pk}))

        self.assertFalse(response.context['is_owner'])

    def test_user_details__when_user_has_no_pets__expect_emtpy_pets(self):
        user = self.create_user_and_login(self.VALID_USER_DATA)
        response = self.client.get(reverse('account details', kwargs={'pk': user.pk}))

        self.assertEqual(0, len(response.context['pets']))

    def test_user_details_when_user_has_pets_no_photos__expect_pets_and_empty_photos(self):
        user = self.create_user_and_login(self.VALID_USER_DATA)
        create_pets(user, 2)
        response = self.client.get(reverse('account details', kwargs={'pk': user.pk}))
        self.assertEqual(2, len(response.context['pets']))
        self.assertEqual(0, len(response.context['photos']))

    def test_user_details_when_user_has_pets_and_photos__expect_pets_and_photos(self):
        user = self.create_user_and_login(self.VALID_USER_DATA)
        create_pets(user, 2)
        create_photos(user, 3)
        response = self.client.get(reverse('account details', kwargs={'pk': user.pk}))
        self.assertEqual(2, len(response.context['pets']))
        self.assertEqual(3, len(response.context['photos']))
