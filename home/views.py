from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseForbidden
from django.urls import reverse
from .models import TodoList, TodoItem


@login_required
def home(request):
    todo_lists = TodoList.objects.filter(user=request.user)
    selected_list = request.GET.get('list_id')

    if selected_list:
        try:
            current_list = TodoList.objects.get(
                id=selected_list, user=request.user)
        except TodoList.DoesNotExist:
            current_list = todo_lists.first()
    else:
        current_list = todo_lists.first()

    if current_list:
        items = TodoItem.objects.filter(todo_list=current_list)
    else:
        items = TodoItem.objects.none()

    completed_items = items.filter(completed=True)
    incomplete_items = items.filter(completed=False)

    context = {
        'todo_lists': todo_lists,
        'current_list': current_list,
        'completed_items': completed_items,
        'incomplete_items': incomplete_items,
    }

    return render(request, 'home/home.html', context)


@login_required
@require_http_methods(["POST"])
def create_todo_list(request):
    title = request.POST.get('title', '').strip()
    description = request.POST.get('description', '').strip()

    if title:
        TodoList.objects.create(
            title=title,
            description=description if description else None,
            user=request.user
        )

    return redirect('home')


@login_required
@require_http_methods(["POST"])
def add_todo_item(request):
    list_id = request.POST.get('list_id')
    item_text = request.POST.get('item_text', '').strip()

    if list_id and item_text:
        todo_list = get_object_or_404(TodoList, id=list_id, user=request.user)
        TodoItem.objects.create(
            todo_list=todo_list,
            item_text=item_text
        )

    if list_id:
        return redirect(reverse('home') + f'?list_id={list_id}')
    return redirect('home')


@login_required
@require_http_methods(["POST"])
def edit_todo_item(request):
    item_id = request.POST.get('item_id')
    item_text = request.POST.get('item_text', '').strip()
    list_id = request.POST.get('list_id')

    if item_id and item_text:
        todo_item = get_object_or_404(TodoItem, id=item_id)

        # Check if user owns this item
        if todo_item.todo_list.user != request.user:
            return HttpResponseForbidden()

        todo_item.item_text = item_text
        todo_item.save()

    if list_id:
        return redirect(reverse('home') + f'?list_id={list_id}')
    return redirect('home')


@login_required
@require_http_methods(["POST"])
def delete_todo_item(request):
    item_id = request.POST.get('item_id')
    list_id = request.POST.get('list_id')

    if item_id:
        todo_item = get_object_or_404(TodoItem, id=item_id)

        # Check if user owns this item
        if todo_item.todo_list.user != request.user:
            return HttpResponseForbidden()

        todo_item.delete()

    if list_id:
        return redirect(reverse('home') + f'?list_id={list_id}')
    return redirect('home')


@login_required
@require_http_methods(["POST"])
def toggle_todo_item(request):
    item_id = request.POST.get('item_id')
    list_id = request.POST.get('list_id')

    if item_id:
        todo_item = get_object_or_404(TodoItem, id=item_id)

        # Check if user owns this item
        if todo_item.todo_list.user != request.user:
            return HttpResponseForbidden()

        todo_item.completed = not todo_item.completed
        todo_item.save()

    if list_id:
        return redirect(reverse('home') + f'?list_id={list_id}')
    return redirect('home')


@login_required
@require_http_methods(["POST"])
def clear_completed_tasks(request):
    list_id = request.POST.get('list_id')

    if list_id:
        todo_list = get_object_or_404(TodoList, id=list_id, user=request.user)
        TodoItem.objects.filter(todo_list=todo_list, completed=True).delete()
        return redirect(reverse('home') + f'?list_id={list_id}')

    return redirect('home')


@login_required
@require_http_methods(["POST"])
def rename_todo_list(request):
    list_id = request.POST.get('list_id')
    title = request.POST.get('title', '').strip()

    if list_id and title:
        todo_list = get_object_or_404(TodoList, id=list_id, user=request.user)
        todo_list.title = title
        todo_list.save()

    if list_id:
        return redirect(reverse('home') + f'?list_id={list_id}')
    return redirect('home')


@login_required
@require_http_methods(["POST"])
def delete_todo_list(request):
    list_id = request.POST.get('list_id')

    if list_id:
        todo_list = get_object_or_404(TodoList, id=list_id, user=request.user)
        todo_list.delete()

    return redirect('home')
