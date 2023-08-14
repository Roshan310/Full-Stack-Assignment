from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.get_tasks, name='tasks'),
    path('tasks/<str:id>', views.get_task, name='task'),
    path('tasks/add/', views.create_task, name='add-task'),
    path('tasks/<str:id>/delete', views.delete_task, name='delete-task'),
    path('tasks/<str:id>/update', views.update_task, name='update-task')
]
