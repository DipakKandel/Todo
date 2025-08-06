from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Task
from accounts.models import User

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser@example.com',
            email='testuser@example.com',
            name='Test User',
            password='testpass123'
        )
    
    def test_create_task(self):
        """Test creating a new task"""
        task = Task.objects.create(
            task='Test task',
            user=self.user,
            is_completed=False
        )
        self.assertEqual(task.task, 'Test task')
        self.assertEqual(task.user, self.user)
        self.assertFalse(task.is_completed)
    
    def test_task_str_representation(self):
        """Test task string representation"""
        task = Task.objects.create(
            task='Test task',
            user=self.user,
            is_completed=False
        )
        self.assertEqual(str(task), 'Test task')
    
    def test_mark_task_complete(self):
        """Test marking a task as complete"""
        task = Task.objects.create(
            task='Test task',
            user=self.user,
            is_completed=False
        )
        task.is_completed = True
        task.save()
        self.assertTrue(task.is_completed)

class TasksViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser@example.com',
            email='testuser@example.com',
            name='Test User',
            password='testpass123'
        )
        self.home_url = reverse('home')
        self.add_task_url = reverse('addTask')
    
    def test_home_page_loads(self):
        """Test that home page loads correctly"""
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
    
    def test_add_task_authenticated_user(self):
        """Test adding task for authenticated user"""
        self.client.force_login(self.user)
        task_data = {'oneTask': 'New test task'}
        response = self.client.post(self.add_task_url, task_data)
        self.assertEqual(response.status_code, 302)  # Redirect to home
        self.assertTrue(Task.objects.filter(task='New test task', user=self.user).exists())
    
    def test_add_task_guest_user(self):
        """Test adding task for guest user"""
        task_data = {'oneTask': 'Guest test task'}
        response = self.client.post(self.add_task_url, task_data)
        self.assertEqual(response.status_code, 302)  # Redirect to home
        
        # Check if task is in session
        session = self.client.session
        self.assertIn('guest_tasks', session)
        guest_tasks = session['guest_tasks']
        self.assertEqual(len(guest_tasks), 1)
        self.assertEqual(guest_tasks[0]['task'], 'Guest test task')
    
    def test_add_empty_task(self):
        """Test adding empty task"""
        task_data = {'oneTask': ''}
        response = self.client.post(self.add_task_url, task_data)
        self.assertEqual(response.status_code, 302)  # Redirect to home
        self.assertEqual(Task.objects.count(), 0)  # No task created
    
    def test_mark_task_done_authenticated(self):
        """Test marking task as done for authenticated user"""
        self.client.force_login(self.user)
        task = Task.objects.create(
            task='Test task',
            user=self.user,
            is_completed=False
        )
        
        response = self.client.get(reverse('markAsDone', args=[task.id]))
        self.assertEqual(response.status_code, 302)  # Redirect to home
        
        # Check if task is marked as complete
        task.refresh_from_db()
        self.assertTrue(task.is_completed)
    
    def test_delete_task_authenticated(self):
        """Test deleting task for authenticated user"""
        self.client.force_login(self.user)
        task = Task.objects.create(
            task='Test task',
            user=self.user,
            is_completed=False
        )
        
        response = self.client.get(reverse('deleteTask', args=[task.id]))
        self.assertEqual(response.status_code, 302)  # Redirect to home
        self.assertFalse(Task.objects.filter(id=task.id).exists())
    
    def test_edit_task_authenticated(self):
        """Test editing task for authenticated user"""
        self.client.force_login(self.user)
        task = Task.objects.create(
            task='Original task',
            user=self.user,
            is_completed=False
        )
        
        edit_data = {'oneTask': 'Updated task'}
        response = self.client.post(reverse('editTask', args=[task.id]), edit_data)
        self.assertEqual(response.status_code, 302)  # Redirect to home
        
        # Check if task is updated
        task.refresh_from_db()
        self.assertEqual(task.task, 'Updated task')
    
    def test_guest_mark_task_done(self):
        """Test marking task as done for guest user"""
        # Add task to session first
        session = self.client.session
        session['guest_tasks'] = [
            {'task': 'Guest task', 'is_completed': False}
        ]
        session.save()
        
        response = self.client.get(reverse('guest_mark_done', args=[0]))
        self.assertEqual(response.status_code, 302)  # Redirect to home
        
        # Check if task is marked as complete in session
        session = self.client.session
        guest_tasks = session['guest_tasks']
        self.assertTrue(guest_tasks[0]['is_completed'])
    
    def test_guest_delete_task(self):
        """Test deleting task for guest user"""
        # Add task to session first
        session = self.client.session
        session['guest_tasks'] = [
            {'task': 'Guest task', 'is_completed': False}
        ]
        session.save()
        
        response = self.client.get(reverse('guest_delete_task', args=[0]))
        self.assertEqual(response.status_code, 302)  # Redirect to home
        
        # Check if task is removed from session
        session = self.client.session
        guest_tasks = session['guest_tasks']
        self.assertEqual(len(guest_tasks), 0)
    
    def test_guest_edit_task(self):
        """Test editing task for guest user"""
        # Add task to session first
        session = self.client.session
        session['guest_tasks'] = [
            {'task': 'Original guest task', 'is_completed': False}
        ]
        session.save()
        
        edit_data = {'oneTask': 'Updated guest task'}
        response = self.client.post(reverse('guest_edit_task', args=[0]), edit_data)
        self.assertEqual(response.status_code, 302)  # Redirect to home
        
        # Check if task is updated in session
        session = self.client.session
        guest_tasks = session['guest_tasks']
        self.assertEqual(guest_tasks[0]['task'], 'Updated guest task')
    
    def test_unauthorized_task_access(self):
        """Test that users cannot access other users' tasks"""
        other_user = User.objects.create_user(
            username='other@example.com',
            email='other@example.com',
            name='Other User',
            password='testpass123'
        )
        
        # Create task for other user
        task = Task.objects.create(
            task='Other user task',
            user=other_user,
            is_completed=False
        )
        
        # Try to access with different user
        self.client.force_login(self.user)
        response = self.client.get(reverse('deleteTask', args=[task.id]))
        self.assertEqual(response.status_code, 302)  # Redirect to home
        
        # Task should still exist
        self.assertTrue(Task.objects.filter(id=task.id).exists())
