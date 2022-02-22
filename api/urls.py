from django.urls import  path
from . import views

urlpatterns = [
    path('', views.apiOverView, name = "api-overView"),
    path('task-list', views.task_list, name = "task-list"),
    path('task-list/<str:pk>/', views.task_detail_list, name = "task-detail-list"),
    path('task-create', views.task_create, name = "task-create"),
    path('task-update/<str:pk>/', views.task_update, name = "task-update"),
    path('task-delete/<str:pk>/', views.task_delete, name = "task-delete"),
]