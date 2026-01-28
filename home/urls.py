from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('create-list/', views.create_todo_list, name='create_todo_list'),
    path('add-item/', views.add_todo_item, name='add_todo_item'),
    path('edit-item/', views.edit_todo_item, name='edit_todo_item'),
    path('delete-item/', views.delete_todo_item, name='delete_todo_item'),
    path('toggle-item/', views.toggle_todo_item, name='toggle_todo_item'),
]
