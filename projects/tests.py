from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from projects.models import Project, Task


class ProjectCreateTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="owner",
            password="test-password",
        )

    def test_authenticated_user_can_create_project(self):
        # Arrange
        self.client.force_login(self.user)

        # Act
        response = self.client.post(
            reverse("project-create"),
            {"name": "Projeto testado"},
        )

        # Assert
        self.assertRedirects(response, reverse("project-list"))
        project = Project.objects.get()
        self.assertEqual(project.name, "Projeto testado")
        self.assertEqual(project.owner, self.user)

    def test_empty_name_does_not_create_project(self):
        # Arrange
        self.client.force_login(self.user)

        # Act
        response = self.client.post(
            reverse("project-create"),
            {"name": ""},
        )

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response.context["form"],
            "name",
            "This field is required.",
        )
        self.assertFalse(Project.objects.exists())

    def test_anonymous_user_cannot_create_project(self):
        # Arrange
        create_url = reverse("project-create")
        login_url = reverse("login")

        # Act
        response = self.client.post(
            create_url,
            {"name": "Projeto indevido"},
        )

        # Assert
        self.assertRedirects(response, f"{login_url}?next={create_url}")
        self.assertFalse(Project.objects.exists())


class ProjectPermissionTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.owner = User.objects.create_user(
            username="owner-a",
            password="test-password",
        )
        self.other_user = User.objects.create_user(
            username="user-b",
            password="test-password",
        )
        self.project = Project.objects.create(
            name="Projeto do owner",
            owner=self.owner,
        )

    def test_other_user_cannot_edit_project(self):
        # Arrange
        self.client.force_login(self.other_user)
        update_url = reverse(
            "project-update",
            kwargs={"pk": self.project.pk},
        )

        # Act
        response = self.client.post(
            update_url,
            {"name": "Nome alterado indevidamente"},
        )

        # Assert
        self.assertEqual(response.status_code, 404)
        self.project.refresh_from_db()
        self.assertEqual(self.project.name, "Projeto do owner")

    def test_user_only_sees_own_projects(self):
        # Arrange
        own_project = Project.objects.create(
            name="Projeto do user B",
            owner=self.other_user,
        )
        self.client.force_login(self.other_user)

        # Act
        response = self.client.get(reverse("project-list"))

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, own_project.name)
        self.assertNotContains(response, self.project.name)

    def test_owner_can_edit_own_project(self):
        # Arrange
        self.client.force_login(self.owner)
        update_url = reverse(
            "project-update",
            kwargs={"pk": self.project.pk},
        )

        # Act
        response = self.client.post(
            update_url,
            {"name": "Projeto atualizado"},
        )

        # Assert
        self.assertRedirects(response, reverse("project-detail", kwargs={"pk": self.project.pk}))
        self.project.refresh_from_db()
        self.assertEqual(self.project.name, "Projeto atualizado")
        self.assertEqual(Project.objects.count(), 1)


class ProjectListQueryTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="owner",
            password="test-password",
        )
        self.project_with_tasks = Project.objects.create(
            name="Projeto com tarefas",
            owner=self.user,
        )
        Project.objects.create(
            name="Projeto vazio",
            owner=self.user,
        )
        Task.objects.create(
            project=self.project_with_tasks,
            title="Primeira Tarefa",
        )
        Task.objects.create(
            project=self.project_with_tasks,
            title="Segunda tarefa",
        )

    def test_list_displays_task_counts_without_n_plus_one(self):
        # Arrange
        self.client.force_login(self.user)

        # Act
        with self.assertNumQueries(3):
            response = self.client.get(reverse("project-list"))

        # Assert
        self.assertContains(response, "2 tarefas")
        self.assertContains(response, "0 tarefas")
