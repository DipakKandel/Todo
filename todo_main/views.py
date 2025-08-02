from django.shortcuts import render
from tasks.models import Task
def home(request):  
    incomplete_tasks = Task.objects.filter(is_completed=False).order_by("-updated_at")
    incomplete_message = None
    if incomplete_tasks.count() == 0:
        incomplete_message = "No tasks to do today"
    
    complete_tasks = Task.objects.filter(is_completed=True, is_archived=False).order_by("-updated_at")
    complete_message = None
    if complete_tasks.count() == 0:
        complete_message = "Lets do more tasks"
    
    context = {
        "todo": incomplete_tasks, 
        "done": complete_tasks,
        "incomplete_message": incomplete_message,
        "complete_message": complete_message
    }
    print(context)
    return render(request,"home.html",context)