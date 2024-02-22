from django.urls import path

from . import views

urlpatterns = [
    path("tasks/", views.TasksList.as_view(), name="tasks"),
    path("tasks/<int:pk>", views.TaskDetail.as_view(), name="task"),
    path("performers/", views.PerformersList.as_view(), name="performers"),
    path("performers/<int:pk>", views.PerformerDetail.as_view(), name="performer"),
]
