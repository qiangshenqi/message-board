from http.client import responses

from django.test import TestCase
from django.urls import reverse

from .models import Post

# Create your tests here.


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!")

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")

    def test_ulr_exits_at_correct_location(self):
        responses = self.client.get("/")
        self.assertEqual(responses.status_code, 200)

    # def test_url_available_by_name(self):
    #     responses = self.client.get(reverse("home"))
    #     self.assertEqual(responses.status_code, 200)
    #
    # def test_template_name_correct(self):
    #     responses = self.client.get(reverse("home"))
    #     self.assertTemplateUsed(responses, "home.html")
    #
    # def test_template_content(self):
    #     responses = self.client.get(reverse("home"))
    #     self.assertContains(responses, "This is a test!")

    def test_homepage(self):
        responses = self.client.get(reverse("home"))
        self.assertEqual(responses.status_code, 200)
        self.assertTemplateUsed(responses, "home.html")
        self.assertContains(responses, "This is a test!")
