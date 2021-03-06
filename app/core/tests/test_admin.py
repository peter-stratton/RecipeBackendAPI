from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='adminuser@example.com',
            password='password123'
        )
        self.client.force_login(self.admin_user)
        self.test_user = get_user_model().objects.create_user(
            email='testuser@example.com',
            password='pass123',
            name='Test User'
        )

    def test_users_listed_on_user_page(self):
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.test_user.name)
        self.assertContains(res, self.test_user.email)

    def test_users_change_page_resolves_correctly(self):
        url = reverse('admin:core_user_change', args=[self.test_user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page_resolves_correctly(self):
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
