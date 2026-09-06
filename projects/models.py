from django.conf import settings
from django.db import models


class ProjectQuerySet(models.QuerySet):
    def owned_by(self, user):
        return self.filter(owner=user)

    def with_task_count(self):
        return self.annotate(task_count=models.Count("tasks"))


class Project(models.Model):
    objects = ProjectQuerySet.as_manager()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="projects",
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    class Status(models.TextChoices):
        TODO = "todo", "A fazer"
        IN_PROGRESS = "in_progress", "Em andamento"
        DONE = "done", "Concluída"

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    title = models.CharField(max_length=200)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.TODO,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(status__in=["todo", "in_progress", "done"]),
                name="task_status_valid",
            ),
        ]

    def __str__(self):
        return self.title
