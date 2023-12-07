from django.test import TestCase
from django.urls import reverse

from .views import index, aaa, bbb

# Create your tests here.

class ViewsTests(TestCase):
    
    
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    
    def test_aaa_view(self):
        response = self.client.get(reverse('aaa'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'aaa.html')
    
    
    def test_bbb_view(self):
        response = self.client.get(reverse('bbb'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bbb.html')
        
    
    def test_hello_viw(self):
        response = self.client.get(reverse('hello'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello, world. Hello.')
        