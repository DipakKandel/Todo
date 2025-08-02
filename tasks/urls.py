from django.urls import path
from . import views
urlpatterns = [
    path("add/",views.addTask,name="addTask"),
    path("delete/<int:id>/",views.deleteTask,name="deleteTask"),
    path("mark-as-done/<int:id>/",views.markAsDone,name="markAsDone"),  
    path("archive/<int:id>/",views.archiveTask,name="archiveTask"),
    path("revert/<int:id>/",views.revertTask,name="revertTask"),
    path("edit/<int:id>/",views.editTask,name="editTask"),
]
