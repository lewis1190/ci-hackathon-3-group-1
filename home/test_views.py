from typing import cast
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import TodoList, TodoItem


class TodoViewsTestCase(TestCase):
    """Test cases for all view functions in home app"""

    def setUp(self):
        """Set up test client and test data"""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.other_user = User.objects.create_user(
            username='otheruser',
            email='other@example.com',
            password='testpass123'
        )
        self.todo_list = TodoList.objects.create(
            title='Test List',
            description='Test Description',
            user=self.user
        )
        self.other_user_list = TodoList.objects.create(
            title='Other List',
            user=self.other_user
        )
        self.other_user_item = TodoItem.objects.create(
            todo_list=self.other_user_list,
            item_text='Other User Item'
        )
        self.todo_item = TodoItem.objects.create(
            todo_list=self.todo_list,
            item_text='Test Item'
        )
        self.completed_item = TodoItem.objects.create(
            todo_list=self.todo_list,
            item_text='Completed Item',
            completed=True
        )

    # ==================== Home View Tests ====================
    def test_home_view_requires_login(self):
        """Test that home view requires authentication"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)
        redirect_response = cast(HttpResponseRedirect, response)
        self.assertTrue(redirect_response.url.startswith('/accounts/login'))

    def test_home_view_loads_with_login(self):
        """Test home view loads successfully for authenticated user"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/home.html')

    def test_home_view_contains_user_lists(self):
        """Test that home view displays only user's todo lists"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('home'))
        self.assertIn('todo_lists', response.context)
        self.assertEqual(len(response.context['todo_lists']), 1)
        self.assertEqual(response.context['todo_lists'][0], self.todo_list)

    def test_home_view_does_not_show_other_users_lists(self):
        """Test that home view does not display other users' lists"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('home'))
        self.assertNotIn(self.other_user_list, response.context['todo_lists'])

    def test_home_view_sets_current_list_to_first(self):
        """Test that current_list defaults to first list"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.context['current_list'], self.todo_list)

    def test_home_view_with_selected_list_id(self):
        """Test home view when list_id parameter is provided"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(
            reverse('home'), {'list_id': self.todo_list.pk})
        self.assertEqual(response.context['current_list'], self.todo_list)

    def test_home_view_with_invalid_list_id(self):
        """Test home view falls back to first list with invalid list_id"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('home'), {'list_id': 99999})
        self.assertEqual(response.context['current_list'], self.todo_list)

    def test_home_view_separates_completed_and_incomplete_items(self):
        """
        Test that items are correctly separated into completed and incomplete
        """
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('home'))
        self.assertEqual(len(response.context['incomplete_items']), 1)
        self.assertEqual(len(response.context['completed_items']), 1)
        self.assertEqual(
            response.context['incomplete_items'][0], self.todo_item)
        self.assertEqual(
            response.context['completed_items'][0], self.completed_item)

    def test_home_view_no_lists_for_new_user(self):
        """Test home view for user with no todo lists"""
        User.objects.create_user(
            username='newuser',
            email='new@example.com',
            password='testpass123'
        )
        self.client.login(username='newuser', password='testpass123')
        response = self.client.get(reverse('home'))
        self.assertEqual(len(response.context['todo_lists']), 0)
        self.assertIsNone(response.context['current_list'])

    # ==================== Create Todo List Tests ====================
    def test_create_todo_list_requires_login(self):
        """Test that create_todo_list requires authentication"""
        response = self.client.post(reverse('create_todo_list'))
        self.assertEqual(response.status_code, 302)
        redirect_response = cast(HttpResponseRedirect, response)
        self.assertTrue(redirect_response.url.startswith('/accounts/login'))

    def test_create_todo_list_requires_post(self):
        """Test that create_todo_list only accepts POST requests"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('create_todo_list'))
        self.assertEqual(response.status_code, 405)

    def test_create_todo_list_success(self):
        """Test successful creation of todo list"""
        self.client.login(username='testuser', password='testpass123')
        initial_count = TodoList.objects.filter(user=self.user).count()
        response = self.client.post(reverse('create_todo_list'), {
            'title': 'New List',
            'description': 'New Description'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            TodoList.objects.filter(user=self.user).count(),
            initial_count + 1
        )
        new_list = TodoList.objects.latest('id')
        self.assertEqual(new_list.title, 'New List')
        self.assertEqual(new_list.description, 'New Description')
        self.assertEqual(new_list.user, self.user)

    def test_create_todo_list_without_description(self):
        """Test creating todo list with only title"""
        self.client.login(username='testuser', password='testpass123')
        self.client.post(reverse('create_todo_list'), {
            'title': 'New List'
        })
        new_list = TodoList.objects.latest('id')
        self.assertIsNone(new_list.description)

    def test_create_todo_list_without_title(self):
        """Test that todo list is not created without title"""
        self.client.login(username='testuser', password='testpass123')
        initial_count = TodoList.objects.filter(user=self.user).count()
        self.client.post(reverse('create_todo_list'), {
            'title': '',
            'description': 'No Title'
        })
        self.assertEqual(
            TodoList.objects.filter(user=self.user).count(),
            initial_count
        )

    def test_create_todo_list_with_whitespace_title(self):
        """Test that whitespace-only title is treated as empty"""
        self.client.login(username='testuser', password='testpass123')
        initial_count = TodoList.objects.filter(user=self.user).count()
        self.client.post(reverse('create_todo_list'), {
            'title': '   '
        })
        self.assertEqual(
            TodoList.objects.filter(user=self.user).count(),
            initial_count
        )

    # ==================== Add Todo Item Tests ====================
    def test_add_todo_item_requires_login(self):
        """Test that add_todo_item requires authentication"""
        response = self.client.post(reverse('add_todo_item'))
        self.assertEqual(response.status_code, 302)
        redirect_response = cast(HttpResponseRedirect, response)
        self.assertTrue(redirect_response.url.startswith('/accounts/login'))

    def test_add_todo_item_requires_post(self):
        """Test that add_todo_item only accepts POST requests"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('add_todo_item'))
        self.assertEqual(response.status_code, 405)

    def test_add_todo_item_success(self):
        """Test successful addition of todo item"""
        self.client.login(username='testuser', password='testpass123')
        initial_count = TodoItem.objects.filter(
            todo_list=self.todo_list).count()
        response = self.client.post(reverse('add_todo_item'), {
            'list_id': self.todo_list.pk,
            'item_text': 'New Item'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            TodoItem.objects.filter(todo_list=self.todo_list).count(),
            initial_count + 1
        )
        new_item = TodoItem.objects.latest('id')
        self.assertEqual(new_item.item_text, 'New Item')
        self.assertFalse(new_item.completed)

    def test_add_todo_item_without_list_id(self):
        """Test that item is not added without list_id"""
        self.client.login(username='testuser', password='testpass123')
        initial_count = TodoItem.objects.count()
        self.client.post(reverse('add_todo_item'), {
            'item_text': 'New Item'
        })
        self.assertEqual(TodoItem.objects.count(), initial_count)

    def test_add_todo_item_without_text(self):
        """Test that item is not added without item_text"""
        self.client.login(username='testuser', password='testpass123')
        initial_count = TodoItem.objects.count()
        self.client.post(reverse('add_todo_item'), {
            'list_id': self.todo_list.pk
        })
        self.assertEqual(TodoItem.objects.count(), initial_count)

    def test_add_todo_item_with_whitespace_text(self):
        """Test that whitespace-only text is treated as empty"""
        self.client.login(username='testuser', password='testpass123')
        initial_count = TodoItem.objects.count()
        self.client.post(reverse('add_todo_item'), {
            'list_id': self.todo_list.pk,
            'item_text': '   '
        })
        self.assertEqual(TodoItem.objects.count(), initial_count)

    def test_add_todo_item_with_nonexistent_list(self):
        """Test adding item to nonexistent list raises 404"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('add_todo_item'), {
            'list_id': 99999,
            'item_text': 'New Item'
        })
        self.assertEqual(response.status_code, 404)

    def test_add_todo_item_to_other_users_list(self):
        """Test that user cannot add item to other user's list"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('add_todo_item'), {
            'list_id': self.other_user_list.pk,
            'item_text': 'Hacked Item'
        })
        self.assertEqual(response.status_code, 404)

    def test_add_todo_item_redirects_with_list_id(self):
        """Test that response redirects with list_id parameter"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('add_todo_item'), {
            'list_id': self.todo_list.pk,
            'item_text': 'New Item'
        }, follow=False)
        redirect_response = cast(HttpResponseRedirect, response)
        self.assertTrue(
            redirect_response.url.startswith(reverse('home')) and
            f'list_id={self.todo_list.pk}' in redirect_response.url
        )

    # ==================== Edit Todo Item Tests ====================
    def test_edit_todo_item_requires_login(self):
        """Test that edit_todo_item requires authentication"""
        response = self.client.post(reverse('edit_todo_item'))
        self.assertEqual(response.status_code, 302)

    def test_edit_todo_item_requires_post(self):
        """Test that edit_todo_item only accepts POST requests"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('edit_todo_item'))
        self.assertEqual(response.status_code, 405)

    def test_edit_todo_item_success(self):
        """Test successful editing of todo item"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('edit_todo_item'), {
            'item_id': self.todo_item.pk,
            'item_text': 'Updated Item',
            'list_id': self.todo_list.pk
        })
        self.assertEqual(response.status_code, 302)
        self.todo_item.refresh_from_db()
        self.assertEqual(self.todo_item.item_text, 'Updated Item')

    def test_edit_todo_item_without_text(self):
        """Test that item is not updated without item_text"""
        self.client.login(username='testuser', password='testpass123')
        original_text = self.todo_item.item_text
        self.client.post(reverse('edit_todo_item'), {
            'item_id': self.todo_item.pk,
            'list_id': self.todo_list.pk
        })
        self.todo_item.refresh_from_db()
        self.assertEqual(self.todo_item.item_text, original_text)

    def test_edit_todo_item_other_user_forbidden(self):
        """Test that user cannot edit other user's item"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('edit_todo_item'), {
            'item_id': self.other_user_item.pk,
            'item_text': 'Hacked Text',
            'list_id': self.other_user_list.pk
        })
        self.assertEqual(response.status_code, 403)

    def test_edit_todo_item_nonexistent(self):
        """Test editing nonexistent item raises 404"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('edit_todo_item'), {
            'item_id': 99999,
            'item_text': 'New Text',
            'list_id': self.todo_list.pk
        })
        self.assertEqual(response.status_code, 404)

    # ==================== Delete Todo Item Tests ====================
    def test_delete_todo_item_requires_login(self):
        """Test that delete_todo_item requires authentication"""
        response = self.client.post(reverse('delete_todo_item'))
        self.assertEqual(response.status_code, 302)

    def test_delete_todo_item_requires_post(self):
        """Test that delete_todo_item only accepts POST requests"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('delete_todo_item'))
        self.assertEqual(response.status_code, 405)

    def test_delete_todo_item_success(self):
        """Test successful deletion of todo item"""
        self.client.login(username='testuser', password='testpass123')
        item_id = self.todo_item.pk
        response = self.client.post(reverse('delete_todo_item'), {
            'item_id': item_id,
            'list_id': self.todo_list.pk
        })
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(TodoItem.DoesNotExist):
            TodoItem.objects.get(id=item_id)

    def test_delete_todo_item_other_user_forbidden(self):
        """Test that user cannot delete other user's item"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('delete_todo_item'), {
            'item_id': self.other_user_item.pk,
            'list_id': self.other_user_list.pk
        })
        self.assertEqual(response.status_code, 403)
        self.other_user_item.refresh_from_db()  # Should not raise

    def test_delete_todo_item_nonexistent(self):
        """Test deleting nonexistent item raises 404"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('delete_todo_item'), {
            'item_id': 99999,
            'list_id': self.todo_list.pk
        })
        self.assertEqual(response.status_code, 404)

    # ==================== Toggle Todo Item Tests ====================
    def test_toggle_todo_item_requires_login(self):
        """Test that toggle_todo_item requires authentication"""
        response = self.client.post(reverse('toggle_todo_item'))
        self.assertEqual(response.status_code, 302)

    def test_toggle_todo_item_requires_post(self):
        """Test that toggle_todo_item only accepts POST requests"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('toggle_todo_item'))
        self.assertEqual(response.status_code, 405)

    def test_toggle_todo_item_incomplete_to_complete(self):
        """Test toggling incomplete item to complete"""
        self.client.login(username='testuser', password='testpass123')
        self.assertFalse(self.todo_item.completed)
        response = self.client.post(reverse('toggle_todo_item'), {
            'item_id': self.todo_item.pk,
            'list_id': self.todo_list.pk
        })
        self.assertEqual(response.status_code, 302)
        self.todo_item.refresh_from_db()
        self.assertTrue(self.todo_item.completed)

    def test_toggle_todo_item_complete_to_incomplete(self):
        """Test toggling complete item to incomplete"""
        self.client.login(username='testuser', password='testpass123')
        self.assertTrue(self.completed_item.completed)
        response = self.client.post(reverse('toggle_todo_item'), {
            'item_id': self.completed_item.pk,
            'list_id': self.todo_list.pk
        })
        self.assertEqual(response.status_code, 302)
        self.completed_item.refresh_from_db()
        self.assertFalse(self.completed_item.completed)

    def test_toggle_todo_item_other_user_forbidden(self):
        """Test that user cannot toggle other user's item"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('toggle_todo_item'), {
            'item_id': self.other_user_item.pk,
            'list_id': self.other_user_list.pk
        })
        self.assertEqual(response.status_code, 403)

    def test_toggle_todo_item_nonexistent(self):
        """Test toggling nonexistent item raises 404"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('toggle_todo_item'), {
            'item_id': 99999,
            'list_id': self.todo_list.pk
        })
        self.assertEqual(response.status_code, 404)

    # ==================== Clear Completed Tasks Tests ====================
    def test_clear_completed_tasks_requires_login(self):
        """Test that clear_completed_tasks requires authentication"""
        response = self.client.post(reverse('clear_completed_tasks'))
        self.assertEqual(response.status_code, 302)

    def test_clear_completed_tasks_requires_post(self):
        """Test that clear_completed_tasks only accepts POST requests"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('clear_completed_tasks'))
        self.assertEqual(response.status_code, 405)

    def test_clear_completed_tasks_success(self):
        """Test successful clearing of completed tasks"""
        self.client.login(username='testuser', password='testpass123')
        # Verify completed item exists
        self.assertEqual(
            TodoItem.objects.filter(
                todo_list=self.todo_list,
                completed=True
            ).count(),
            1
        )
        response = self.client.post(reverse('clear_completed_tasks'), {
            'list_id': self.todo_list.pk
        })
        self.assertEqual(response.status_code, 302)
        # Verify completed item is deleted
        self.assertEqual(
            TodoItem.objects.filter(
                todo_list=self.todo_list,
                completed=True
            ).count(),
            0
        )
        # Verify incomplete item still exists
        self.assertEqual(
            TodoItem.objects.filter(
                todo_list=self.todo_list,
                completed=False
            ).count(),
            1
        )

    def test_clear_completed_tasks_no_completed(self):
        """Test clearing when no completed tasks exist"""
        self.client.login(username='testuser', password='testpass123')
        new_list = TodoList.objects.create(title='Empty List', user=self.user)
        TodoItem.objects.create(todo_list=new_list, item_text='Item 1')
        response = self.client.post(reverse('clear_completed_tasks'), {
            'list_id': new_list.pk
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(TodoItem.objects.filter(
            todo_list=new_list).count(), 1)

    def test_clear_completed_tasks_other_user_forbidden(self):
        """Test that user cannot clear other user's completed tasks"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('clear_completed_tasks'), {
            'list_id': self.other_user_list.pk
        })
        self.assertEqual(response.status_code, 404)

    def test_clear_completed_tasks_nonexistent_list(self):
        """Test clearing completed tasks from nonexistent list raises 404"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('clear_completed_tasks'), {
            'list_id': 99999
        })
        self.assertEqual(response.status_code, 404)

    def test_clear_completed_tasks_without_list_id(self):
        """Test clear_completed_tasks redirects to home without list_id"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(
            reverse('clear_completed_tasks'), follow=False)
        self.assertEqual(response.status_code, 302)
        redirect_response = cast(HttpResponseRedirect, response)
        self.assertEqual(redirect_response.url, reverse('home'))

    # ==================== Rename Todo List Tests ====================
    def test_rename_todo_list_requires_login(self):
        """Test that rename_todo_list requires authentication"""
        response = self.client.post(reverse('rename_todo_list'))
        self.assertEqual(response.status_code, 302)

    def test_rename_todo_list_requires_post(self):
        """Test that rename_todo_list only accepts POST requests"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('rename_todo_list'))
        self.assertEqual(response.status_code, 405)

    def test_rename_todo_list_success(self):
        """Test successful renaming of todo list"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('rename_todo_list'), {
            'list_id': self.todo_list.pk,
            'title': 'Renamed List'
        })
        self.assertEqual(response.status_code, 302)
        self.todo_list.refresh_from_db()
        self.assertEqual(self.todo_list.title, 'Renamed List')

    def test_rename_todo_list_without_title(self):
        """Test that list is not renamed without title"""
        self.client.login(username='testuser', password='testpass123')
        original_title = self.todo_list.title
        self.client.post(reverse('rename_todo_list'), {
            'list_id': self.todo_list.pk
        })
        self.todo_list.refresh_from_db()
        self.assertEqual(self.todo_list.title, original_title)

    def test_rename_todo_list_with_whitespace_title(self):
        """Test that whitespace-only title is treated as empty"""
        self.client.login(username='testuser', password='testpass123')
        original_title = self.todo_list.title
        self.client.post(reverse('rename_todo_list'), {
            'list_id': self.todo_list.pk,
            'title': '   '
        })
        self.todo_list.refresh_from_db()
        self.assertEqual(self.todo_list.title, original_title)

    def test_rename_todo_list_other_user_forbidden(self):
        """Test that user cannot rename other user's list"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('rename_todo_list'), {
            'list_id': self.other_user_list.pk,
            'title': 'Hacked Name'
        })
        self.assertEqual(response.status_code, 404)

    def test_rename_todo_list_nonexistent(self):
        """Test renaming nonexistent list raises 404"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('rename_todo_list'), {
            'list_id': 99999,
            'title': 'New Name'
        })
        self.assertEqual(response.status_code, 404)

    # ==================== Delete Todo List Tests ====================
    def test_delete_todo_list_requires_login(self):
        """Test that delete_todo_list requires authentication"""
        response = self.client.post(reverse('delete_todo_list'))
        self.assertEqual(response.status_code, 302)

    def test_delete_todo_list_requires_post(self):
        """Test that delete_todo_list only accepts POST requests"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('delete_todo_list'))
        self.assertEqual(response.status_code, 405)

    def test_delete_todo_list_success(self):
        """Test successful deletion of todo list"""
        self.client.login(username='testuser', password='testpass123')
        list_id = self.todo_list.pk
        response = self.client.post(reverse('delete_todo_list'), {
            'list_id': list_id
        })
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(TodoList.DoesNotExist):
            TodoList.objects.get(id=list_id)

    def test_delete_todo_list_cascades_items(self):
        """Test that deleting list also deletes its items"""
        self.client.login(username='testuser', password='testpass123')
        list_id = self.todo_list.pk
        item_ids = [item.pk for item in TodoItem.objects.
                    filter(todo_list=self.todo_list)]
        self.client.post(reverse('delete_todo_list'), {
            'list_id': list_id
        })
        # Verify all items are deleted
        for item_id in item_ids:
            with self.assertRaises(TodoItem.DoesNotExist):
                TodoItem.objects.get(id=item_id)

    def test_delete_todo_list_other_user_forbidden(self):
        """Test that user cannot delete other user's list"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('delete_todo_list'), {
            'list_id': self.other_user_list.pk
        })
        self.assertEqual(response.status_code, 404)
        self.other_user_list.refresh_from_db()  # Should not raise

    def test_delete_todo_list_nonexistent(self):
        """Test deleting nonexistent list raises 404"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('delete_todo_list'), {
            'list_id': 99999
        })
        self.assertEqual(response.status_code, 404)
