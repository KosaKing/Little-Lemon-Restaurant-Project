from django.test import TestCase
from restaurant.models import Menu
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setup(self):
        self.menu1 = Menu.objects.create(name='Burger', price=10.00, inventory=2)
        self.menu2 = Menu.objects.create(name='Pizza', price=15.00, inventory=2)
        self.menu3 = Menu.objects.create(name='Sushi', price=20.00, inventory=2)

    def test_getall(self):
        url = reverse('menu-list')
        response = self.client.get(url)
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)