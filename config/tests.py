from django.contrib.auth import SESSION_KEY, get_user_model
from django.test import TestCase
from django.urls import reverse


class HomeViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test-user",
            password="test-password",
        )

    def test_anonymous_user_is_redirected_to_login(self):
        home_url = reverse("home")
        login_url = reverse("login")

        response = self.client.get(home_url)

        self.assertRedirects(response, f"{login_url}?next={home_url}")

    def test_authenticated_user_can_access_home(self):
        home_url = reverse("home")
        self.client.force_login(self.user)

        response = self.client.get(home_url)

        self.assertEqual(response.status_code, 200)

    def test_home_uses_expected_template(self):
        home_url = reverse("home")
        self.client.force_login(self.user)

        response = self.client.get(home_url)

        self.assertTemplateUsed(response, "home.html")

    def test_successful_login_redirects_to_home(self):
        home_url = reverse("home")
        login_url = reverse("login")

        response = self.client.post(
            login_url,
            {
                "username": "test-user",
                "password": "test-password",
            },
        )

        self.assertRedirects(response, home_url)

    def test_logout_ends_session_and_redirects_to_login(self):
        self.client.force_login(self.user)

        response = self.client.post(reverse("logout"))

        self.assertRedirects(response, reverse("login"))
        self.assertNotIn(SESSION_KEY, self.client.session)


class HealthViewTests(TestCase):
    def test_health_endpoint_is_available(self):
        response = self.client.get("/health/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})
