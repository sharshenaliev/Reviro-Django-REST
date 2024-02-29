from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
import factory


User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = 'test_user@mail.com'
    password = factory.PostGenerationMethodCall('set_password', 'test_password')


class TokenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Token

    user = factory.SubFactory(UserFactory)


class TestUser(APITestCase):

    def test_register(self):
        user = UserFactory.build()
        data = {"email": user.username, "password": user.password, "password2": user.password}
        response = self.client.post("/register/", data)
        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_login(self):
        user = UserFactory()
        password = 'test_password'
        data = {"email": user.username, "password": password}
        response = self.client.post("/login/", data)
        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_logout(self):
        token = TokenFactory()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, HTTP_200_OK)
