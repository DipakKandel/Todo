from django.shortcuts import redirect, render
from .models import Task
from datetime import datetime
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

def addTask(request):
    task_text = request.POST.get("oneTask", "").strip()

    if not task_text:
        return redirect("home")

    if request.user.is_authenticated:
        Task.objects.create(task=task_text, user=request.user, is_completed=False)
    else:
        guest_tasks = request.session.get("guest_tasks", [])

        # ✅ Only store as dict
        guest_tasks.append({
            "task": task_text,
            "is_completed": False
        })
        request.session["guest_tasks"] = guest_tasks

    return redirect("home")


@login_required
def deleteTask(request, id):
    try:
        task = Task.objects.get(id=id, user=request.user)
        task.delete()
    except ObjectDoesNotExist:
        pass  # Task doesn't exist or doesn't belong to user
    return redirect("home")


@login_required
def markAsDone(request, id):
    try:
        task = Task.objects.get(id=id, user=request.user)
        task.is_completed = True
        task.save()
    except ObjectDoesNotExist:
        pass  # Task doesn't exist or doesn't belong to user
    return redirect("home")

@login_required
def archiveTask(request, id):
    print("Archiving task")
    try:
        task = Task.objects.get(id=id, user=request.user)
        task.is_archived = True
        task.save()
    except ObjectDoesNotExist:
        pass  # Task doesn't exist or doesn't belong to user
    return redirect("home")

@login_required
def revertTask(request, id):
    print("Reverting task")
    try:
        task = Task.objects.get(id=id, user=request.user)
        task.is_completed = False
        task.save()
    except ObjectDoesNotExist:
        pass  # Task doesn't exist or doesn't belong to user
    return redirect("home")

@login_required
def editTask(request, id):
    if request.method == "POST":
        print("Updating task")
        try:
            task = Task.objects.get(id=id, user=request.user)
            updated_task = request.POST["oneTask"]
            task.task = updated_task
            task.updated_at = datetime.now()
            task.save()
        except ObjectDoesNotExist:
            pass  # Task doesn't exist or doesn't belong to user
        return redirect("home")
    else:
        return redirect("home") 

def guest_mark_done(request, id):
    tasks = request.session.get("guest_tasks", [])
    if 0 <= id < len(tasks):
        tasks[id]["is_completed"] = True
        request.session["guest_tasks"] = tasks
    return redirect("home")


def guest_delete_task(request, id):
    tasks = request.session.get("guest_tasks", [])
    if 0 <= id < len(tasks):
        tasks.pop(id)
        request.session["guest_tasks"] = tasks
    return redirect("home")


def guest_mark_undone(request, id):
    tasks = request.session.get("guest_tasks", [])
    if 0 <= id < len(tasks):
        tasks[id]["is_completed"] = False
        request.session["guest_tasks"] = tasks
    return redirect("home")

def guest_edit_task(request, id):
    if request.method == "POST":
        tasks = request.session.get("guest_tasks", [])
        if 0 <= id < len(tasks):
            updated_task = request.POST["oneTask"]
            tasks[id]["task"] = updated_task
            request.session["guest_tasks"] = tasks
    return redirect("home")

def clear_guest_session(request):
    request.session.clear()
    return redirect("home")