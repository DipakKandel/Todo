from django.shortcuts import render
from tasks.models import Task
import os

# Initialize OpenAI client only if API key is available
try:
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) if os.getenv("OPENAI_API_KEY") else None
except ImportError:
    client = None


def home(request):
    incomplete_tasks = []
    complete_tasks = []
    incomplete_message = None
    complete_message = None
    summary = "No summary available."

    if request.user.is_authenticated:
        # ✅ Logged-in user: Get tasks from DB
        incomplete_tasks = Task.objects.filter(is_completed=False, user=request.user).order_by("-updated_at")
        complete_tasks = Task.objects.filter(is_completed=True, is_archived=False, user=request.user).order_by("-updated_at")

        if not incomplete_tasks.exists():
            incomplete_message = "No tasks to do today"
        if not complete_tasks.exists():
            complete_message = "Let's do more tasks"

        # ✅ Prepare task texts for AI summary
        incomplete_list = [t.task for t in incomplete_tasks]
        complete_list = [t.task for t in complete_tasks]

    else:
        # ✅ Anonymous user: use session
        incomplete_list = []
        complete_list = []
        guest_tasks = request.session.get("guest_tasks", [])
        for i, task in enumerate(guest_tasks):
                task_with_id = {**task, "id": i}
                if task.get("is_completed"):
                    complete_list.append(task_with_id)
                else:
                    incomplete_list.append(task_with_id)
        if not incomplete_list:
                incomplete_message = "No tasks to do today"
        if not complete_list:
                complete_message = "Let's do more tasks"

    # ✅ Generate summary via AI
    if client:
        try:
            prompt = (
                "Give me a one-line summary of my day. "
                "Incomplete tasks: " + str(incomplete_list) +
                " | Completed tasks: " + str(complete_list)
            )
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            summary = response.choices[0].message.content
        except Exception as e:
            print(e)
            summary = "Error in generating summary"
    else:
        summary = "AI summary not available (OpenAI API key not configured)"

    context = {
        "todo": incomplete_tasks if request.user.is_authenticated else incomplete_list,
        "done": complete_tasks if request.user.is_authenticated else complete_list,
        "incomplete_message": incomplete_message,
        "complete_message": complete_message,
        "summary": summary
    }

    return render(request, "home.html", context)
