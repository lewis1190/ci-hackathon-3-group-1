from django.contrib import admin
from .models import TodoList, TodoItem


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'user')
    search_fields = ('title', 'description', 'user__username')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('item_text', 'todo_list', 'completed', 'created_at')
    list_filter = ('completed', 'created_at', 'todo_list')
    search_fields = ('item_text', 'todo_list__title')
    readonly_fields = ('created_at', 'updated_at')
