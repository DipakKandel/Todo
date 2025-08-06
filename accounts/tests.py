from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import User

class UserModelTest(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser@example.com',
            'email': 'testuser@example.com',
            'name': 'Test User',
            'password': 'testpass123'
        }
    
    def test_create_user(self):
        """Test creating a new user"""
        user = User.objects.create_user(
            username=self.user_data['username'],
            email=self.user_data['email'],
            name=self.user_data['name'],
            password=self.user_data['password']
        )
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertEqual(user.name, 'Test User')
        self.assertTrue(user.check_password('testpass123'))
    
    def test_user_str_representation(self):
        """Test user string representation"""
        user = User.objects.create_user(
            username='test@example.com',
            email='test@example.com',
            name='Test User',
            password='testpass123'
        )
        self.assertEqual(str(user), 'Test User')

class AccountsViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register_user')  # Changed to register_user
        self.login_url = reverse('login')
        self.home_url = reverse('home')
        
        self.user_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'password': 'testpass123',
            'confirm_password': 'testpass123'
        }
    
    def test_register_page_loads(self):
        """Test that register page loads correctly"""
        response = self.client.get(reverse('register'))  # Use the register view for GET
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
    
    def test_login_page_loads(self):
        """Test that login page loads correctly"""
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
    
    def test_user_registration_success(self):
        """Test successful user registration"""
        response = self.client.post(self.register_url, self.user_data)
        # Check that user was created successfully
        self.assertTrue(User.objects.filter(email='test@example.com').exists())
        # Check that we get a redirect (302) or success response
        self.assertIn(response.status_code, [200, 302])
    
    def test_user_registration_password_mismatch(self):
        """Test registration with mismatched passwords"""
        self.user_data['confirm_password'] = 'wrongpassword'
        response = self.client.post(self.register_url, self.user_data)
        # Check that no user was created
        self.assertFalse(User.objects.filter(email='test@example.com').exists())
        # Check that we get a redirect (302) or stay on page (200)
        self.assertIn(response.status_code, [200, 302])
    
    def test_user_registration_duplicate_email(self):
        """Test registration with existing email"""
        # Create first user
        User.objects.create_user(
            username='existing@example.com',
            email='existing@example.com',
            name='Existing User',
            password='testpass123'
        )
        
        # Try to register with same email
        self.user_data['email'] = 'existing@example.com'
        response = self.client.post(self.register_url, self.user_data)
        # Check that only one user exists with this email
        self.assertEqual(User.objects.filter(email='existing@example.com').count(), 1)
        # Check that we get a redirect (302) or stay on page (200)
        self.assertIn(response.status_code, [200, 302])
    
    def test_user_login_success(self):
        """Test successful user login"""
        # Create user
        user = User.objects.create_user(
            username='test@example.com',
            email='test@example.com',
            name='Test User',
            password='testpass123'
        )
        
        # Login
        login_data = {
            'email': 'test@example.com',
            'password': 'testpass123'
        }
        response = self.client.post(reverse('login_user'), login_data)
        self.assertEqual(response.status_code, 302)  # Redirect to home
        
        # Check if user is logged in
        response = self.client.get(self.home_url)
        self.assertContains(response, 'Test User')
    
    def test_user_login_invalid_credentials(self):
        """Test login with invalid credentials"""
        login_data = {
            'email': 'nonexistent@example.com',
            'password': 'wrongpassword'
        }
        response = self.client.post(reverse('login_user'), login_data)
        self.assertEqual(response.status_code, 302)  # Redirect to login
