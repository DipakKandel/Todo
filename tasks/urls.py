from django.urls import path
from . import views
urlpatterns = [
    path("add/",views.addTask,name="addTask"),
    path("delete/<int:id>/",views.deleteTask,name="deleteTask"),
    path("mark-as-done/<int:id>/",views.markAsDone,name="markAsDone"),  
    path("archive/<int:id>/",views.archiveTask,name="archiveTask"),
    path("revert/<int:id>/",views.revertTask,name="revertTask"),
    path("edit/<int:id>/",views.editTask,name="editTask"),
    path('guest/mark-done/<int:id>/', views.guest_mark_done, name='guest_mark_done'),
    path('guest/delete/<int:id>/', views.guest_delete_task, name='guest_delete_task'),
    path('guest/mark-undone/<int:id>/', views.guest_mark_undone, name='guest_mark_undone'),
    path('guest/edit/<int:id>/', views.guest_edit_task, name='guest_edit_task'),
    path("clear-session/", views.clear_guest_session, name="clear_session"),
]
