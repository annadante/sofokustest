from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.index, name="list"),
    path('update/<str:pk>?', views.updateTask, name="update_task"),
    path('delete/<str:pk>?', views.deleteTask, name="delete_task"),
    path('moveup/<str:pk>?', views.moveTaskUp, name="move_up"),
    path('movedown/<str:pk>?', views.moveTaskDown, name="move_down"),
]