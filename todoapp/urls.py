from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('delete/<int:taskid>/', views.delete, name = 'delete'),
    path('edit/<int:id>/' , views.edit,name ='edit'),
    path('completed-tasks/', views.task_lists, name='completed_tasks'),
    path('pending-tasks/', views.task_lists, name='pending_tasks'),
    path('expired-tasks/', views.task_lists, name='expired_tasks'),
    path('cbv/', views.tasklistview.as_view(), name = 'cbv')
    # Fix the view name here
]
