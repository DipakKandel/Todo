from django.shortcuts import render
from tasks.models import Task
def home(request):  
    incomplete_tasks = Task.objects.filter(is_completed=False)
    complete_tasks = Task.objects.filter(is_completed=True)
    context = {"todo":incomplete_tasks, "done":complete_tasks}
    print(context)
    return render(request,"home.html",context)