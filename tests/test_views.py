from django.test import TestCase
from Restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title='IceCream', price=80, inventory=100)
        
    def test_getall(self):
        item = Menu.objects.get(title='IceCream')
        self.assertEqual(item.title, 'IceCream')