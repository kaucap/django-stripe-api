from django.test import TestCase
from django.urls import reverse
from app_shop.models import Item


class ShopTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Item.objects.create(
            name='Предмет 1',
            description='Описание предмета',
            price=1000
        )

    def test_if_main_page_works(self):
        response = self.client.get(reverse('main_page'))
        self.assertEqual(response.status_code, 200)

    def test_if_main_page_use_right_template(self):
        response = self.client.get(reverse('main_page'))
        self.assertTemplateUsed(response, 'site/main_page.html')

    def test_if_main_page_use_wrong_template(self):
        response = self.client.get(reverse('main_page'))
        self.assertTemplateNotUsed(response, 'site/success.html')

    def test_if_item_detail_page_works(self):
        item = Item.objects.get(name='Предмет 1')
        response = self.client.get(reverse('item_detail', kwargs={'pk': item.pk}))
        self.assertEqual(response.status_code, 200)

    def test_if_item_detail_page_use_right_template(self):
        item = Item.objects.get(name='Предмет 1')
        response = self.client.get(reverse('item_detail', kwargs={'pk': item.pk}))
        self.assertTemplateUsed(response, 'site/item_detail.html')

    def test_if_item_detail_page_use_wrong_template(self):
        item = Item.objects.get(name='Предмет 1')
        response = self.client.get(reverse('item_detail', kwargs={'pk': item.pk}))
        self.assertTemplateNotUsed(response, 'site/main_page.html')

    def test_if_success_page_works(self):
        response = self.client.get(reverse('success'))
        self.assertEqual(response.status_code, 200)

    def test_if_success_page_use_right_template(self):
        response = self.client.get(reverse('success'))
        self.assertTemplateUsed(response, 'site/success.html')

    def test_if_success_page_use_wrong_template(self):
        response = self.client.get(reverse('success'))
        self.assertTemplateNotUsed(response, 'site/main_page.html')

    def test_if_cancel_page_works(self):
        response = self.client.get(reverse('cancel'))
        self.assertEqual(response.status_code, 200)

    def test_if_cancel_page_use_right_template(self):
        response = self.client.get(reverse('cancel'))
        self.assertTemplateUsed(response, 'site/cancel.html')

    def test_if_cancel_page_use_wrong_template(self):
        response = self.client.get(reverse('cancel'))
        self.assertTemplateNotUsed(response, 'site/main_page.html')
