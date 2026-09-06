from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from projects.forms import ProjectForm
from projects.models import Project


@login_required
def project_list(request):
    projects = Project.objects.owned_by(request.user).with_task_count()
    context = {"projects": projects}
    return render(request, "projects/project_list.html", context)


@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project.objects.owned_by(request.user), pk=pk)
    context = {"project": project}
    return render(request, "projects/project_detail.html", context)


@login_required
def project_update(request, pk):
    project = get_object_or_404(Project.objects.owned_by(request.user), pk=pk)

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)

        if form.is_valid():
            form.save()
            return redirect("project-detail", pk=project.pk)
    else:
        form = ProjectForm(instance=project)

    context = {"form": form, "project": project}
    return render(request, "projects/project_form.html", context)


@login_required
def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)

        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect("project-list")
    else:
        form = ProjectForm()

    context = {"form": form}
    return render(request, "projects/project_form.html", context)
