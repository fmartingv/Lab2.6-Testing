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
            reverse('burros-list'),  # Cambiado de 'burro-list' a 'burros-list'
            self.burro_data,
            format="json"
        )

    def test_api_can_create_a_burro(self):
        print(f"Response status: {self.response.status_code}")
        print(f"Response content: {self.response.content}")
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_burro(self):
        burro = Burro.objects.get()
        response = self.client.get(
            reverse('burros-detail', kwargs={'pk': burro.id}),  # Cambiado de 'burro-detail' a 'burros-detail'
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, burro.nombre)

    def test_api_can_update_burro(self):
        burro = Burro.objects.get()
        change_burro = {'nombre': 'Nuevo nombre'}
        res = self.client.patch(
            reverse('burros-detail', kwargs={'pk': burro.id}),  # Cambiado de 'burro-detail' a 'burros-detail'
            change_burro,
            format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_burro(self):
        burro = Burro.objects.get()
        response = self.client.delete(
            reverse('burros-detail', kwargs={'pk': burro.id}),  # Cambiado de 'burro-detail' a 'burros-detail'
            format='json',
            follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)