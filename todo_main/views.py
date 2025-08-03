from django.shortcuts import render
from tasks.models import Task
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
    )


def home(request):  
    incomplete_tasks = Task.objects.filter(is_completed=False).order_by("-updated_at")
    incomplete_message = None
    if incomplete_tasks.count() == 0:
        incomplete_message = "No tasks to do today"
    
    complete_tasks = Task.objects.filter(is_completed=True, is_archived=False).order_by("-updated_at")
    complete_message = None
    if complete_tasks.count() == 0:
        complete_message = "Lets do more tasks"
    
    try:
        response = client.responses.create(
        model="gpt-4.1",
        # input = "write a one funny joke in a sentence"
        input="just Give me one line summary of my day based on the tasks i have completed and the tasks i have not completed incomplete tasks are : " + str(incomplete_tasks) + "and completed tasks are : " + str(complete_tasks)         )
        Summary = response.output_text
    except Exception as e:
        print(e)
        Summary = "Error in generating summary"

    context = {
        "todo": incomplete_tasks, 
        "done": complete_tasks,
        "incomplete_message": incomplete_message,
        "complete_message": complete_message,
        "summary": Summary
    }
    print(context)
    return render(request,"home.html",context)