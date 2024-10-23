from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Burro
from .serializers import BurroSerializer

class BurroModelTest(TestCase):
    def setUp(self):
        self.burro = Burro.objects.create(
            nombre="Pepito",
            edad=5,
            color="Gris",
            peso=150.5
        )

    def test_burro_creation(self):
        self.assertEqual(self.burro.nombre, "Pepito")
        self.assertEqual(self.burro.edad, 5)
        self.assertEqual(self.burro.color, "Gris")
        self.assertEqual(self.burro.peso, 150.5)

class BurroAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.burro_data = {
            'nombre': 'Juanito',
            'edad': 3,
            'color': 'Marrón',
            'peso': 120.0
        }
        self.response = self.client.post(
            reverse('burro-list'),
            self.burro_data,
            format="json"
        )

    def test_api_can_create_a_burro(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_burro(self):
        burro = Burro.objects.get()
        response = self.client.get(
            reverse('burro-detail', kwargs={'pk': burro.id}),
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, burro.nombre)

    def test_api_can_update_burro(self):
        burro = Burro.objects.get()
        change_burro = {'nombre': 'Nuevo nombre'}
        res = self.client.patch(
            reverse('burro-detail', kwargs={'pk': burro.id}),
            change_burro, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_burro(self):
        burro = Burro.objects.get()
        response = self.client.delete(
            reverse('burro-detail', kwargs={'pk': burro.id}),
            format='json',
            follow=True
        )
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

class SecurityTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_csrf_protection(self):
        response = self.client.post(
            reverse('burro-list'),
            {'nombre': 'Test CSRF'},
            format='json'
        )
        self.assertNotEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_xss_protection(self):
        xss_burro = {
            'nombre': '<script>alert("XSS")</script>',
            'edad': 1,
            'color': 'Negro',
            'peso': 100.0
        }
        response = self.client.post(
            reverse('burro-list'),
            xss_burro,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        burro = Burro.objects.get(id=response.data['id'])
        self.assertNotEqual(burro.nombre, xss_burro['nombre'])