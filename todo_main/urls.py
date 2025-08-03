
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.home,name="home"),
]

# Todo App
urlpatterns += [
    path("tasks/", include("tasks.urls")),
    path("user/", include("accounts.urls")),
]
