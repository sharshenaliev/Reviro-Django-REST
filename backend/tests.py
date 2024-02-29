from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.test import APITestCase
from backend.test_auth import TokenFactory
from backend.models import Product, Establishment
import factory


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('name')
    description = factory.Faker('text')
    price = factory.Faker('pyint', min_value=1, max_value=1000)
    quantity_in_stock = factory.Faker('pyint', min_value=1, max_value=100)


class EstablishmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Establishment

    name = factory.Faker('name')
    description = factory.Faker('text')
    location = "Асанбай, 27/1"
    opening_hour = factory.Faker('time')
    closing_hour = factory.Faker('time')


class TestProduct(APITestCase):

    def test_product_list(self):
        product = ProductFactory()
        expected_data = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": product.id,
                    "name": product.name,
                    "description": product.description,
                    "price": product.price,
                    "quantity_in_stock": product.quantity_in_stock,
                }
            ]
        }
        response = self.client.get("/api/product/")
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_product_post(self):
        product = ProductFactory.build()
        expected_data = {
            "id": 5,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "quantity_in_stock": product.quantity_in_stock,
        }
        token = TokenFactory()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post("/api/product/", data=expected_data)
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(response.data, expected_data)

    def test_product_get(self):
        product = ProductFactory()
        expected_data = {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "quantity_in_stock": product.quantity_in_stock,

        }
        response = self.client.get(f"/api/product/{product.id}/")
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_product_put(self):
        product = ProductFactory()
        expected_data = {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "quantity_in_stock": product.quantity_in_stock,

        }
        token = TokenFactory()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.put(f"/api/product/{product.id}/", data=expected_data)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_product_patch(self):
        product = ProductFactory()
        expected_data = {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "quantity_in_stock": product.quantity_in_stock,

        }
        token = TokenFactory()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.patch(f"/api/product/{product.id}/", data=expected_data)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_product_delete(self):
        token = TokenFactory()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        product = ProductFactory()
        response = self.client.delete(f"/api/product/{product.id}/")
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)


class TestEstablishment(APITestCase):

    def test_establishment_list(self):
        establishment = EstablishmentFactory()
        expected_data = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": establishment.id,
                    "name": establishment.name,
                    "description": establishment.description,
                    "location": establishment.location,
                    "opening_hour": establishment.opening_hour[0:5],
                    "closing_hour": establishment.closing_hour[0:5],
                    "opening_hours": f'{establishment.opening_hour[0:5]} - {establishment.closing_hour[0:5]}',
                }
            ]
        }
        response = self.client.get("/api/establishment/")
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_establishment_post(self):
        establishment = EstablishmentFactory.build()
        expected_data = {
            "id": 5,
            "name": establishment.name,
            "description": establishment.description,
            "location": establishment.location,
            "opening_hour": establishment.opening_hour[0:5],
            "closing_hour": establishment.closing_hour[0:5],
            "opening_hours": f'{establishment.opening_hour[0:5]} - {establishment.closing_hour[0:5]}',
        }
        token = TokenFactory()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post("/api/establishment/", data=expected_data)
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(response.data, expected_data)

    def test_establishment_get(self):
        establishment = EstablishmentFactory()
        expected_data = {
            "id": establishment.id,
            "name": establishment.name,
            "description": establishment.description,
            "location": establishment.location,
            "opening_hour": establishment.opening_hour[0:5],
            "closing_hour": establishment.closing_hour[0:5],
            "opening_hours": f'{establishment.opening_hour[0:5]} - {establishment.closing_hour[0:5]}',
        }
        response = self.client.get(f"/api/establishment/{establishment.id}/")
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_establishment_put(self):
        establishment = EstablishmentFactory()
        expected_data = {
            "id": establishment.id,
            "name": establishment.name,
            "description": establishment.description,
            "location": establishment.location,
            "opening_hour": establishment.opening_hour[0:5],
            "closing_hour": establishment.closing_hour[0:5],
            "opening_hours": f'{establishment.opening_hour[0:5]} - {establishment.closing_hour[0:5]}',
        }
        token = TokenFactory()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.put(f"/api/establishment/{establishment.id}/", data=expected_data)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_establishment_patch(self):
        establishment = EstablishmentFactory()
        expected_data = {
            "id": establishment.id,
            "name": establishment.name,
            "description": establishment.description,
            "location": establishment.location,
            "opening_hour": establishment.opening_hour[0:5],
            "closing_hour": establishment.closing_hour[0:5],
            "opening_hours": f'{establishment.opening_hour[0:5]} - {establishment.closing_hour[0:5]}',
        }
        token = TokenFactory()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.patch(f"/api/establishment/{establishment.id}/", data=expected_data)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_establishment_delete(self):
        token = TokenFactory()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        establishment = EstablishmentFactory()
        response = self.client.delete(f"/api/establishment/{establishment.id}/")
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
