from django.shortcuts import redirect, render
from .models import Task
from datetime import datetime
# Create your views here.
def addTask(request):
  task = request.POST["oneTask"]
  task = task.strip()
  if task != "":
    Task.objects.create(task=task, is_completed=False)
  else:
    print("Task is empty")
  return redirect("home")


def deleteTask(request, id):
  task = Task.objects.get(id=id)
  task.delete()
  return redirect("home")


def markAsDone(request, id):
  task = Task.objects.get(id=id)
  task.is_completed = True
  task.save()
  return redirect("home")

def archiveTask(request, id):
  print("Archiving task")
  task = Task.objects.get(id=id)
  task.is_archived = True
  task.save()
  return redirect("home")

def revertTask(request, id):
  print("Reverting task")
  task = Task.objects.get(id=id)
  task.is_completed = False
  task.save()
  return redirect("home")

def editTask(request, id):
  if request.method == "POST":
    print("Updating task")
    task = Task.objects.get(id=id)
    updated_task = request.POST["oneTask"]
    task.task = updated_task
    task.updated_at = datetime.now()
    task.save()
    return redirect("home")
  else:
    return redirect("home") 