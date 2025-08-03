from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login
# Create your views here.
def register(request):
    return render(request, 'register.html')

def register_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        check_email = User.objects.filter(email=email).exists()
        if check_email:
            return redirect('login')
        else:
          password = request.POST['password']
          confirm_password = request.POST['confirm_password']
          if password == confirm_password:
            user = User.objects.create_user(
                username=email,  # Use email as username
                email=email,
                name=name,
                password=password
            )
            return redirect('login')
          else:
            return redirect('register')

def login_view(request):
    return render(request, 'login.html')

def login_user(request):
   if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)  # Use email as username
        if user is not None:
            login(request, user)  # ✅ this sets the user in session
            print("user is found")
            return redirect('home')
        else:
            print("user is not found")
            return redirect('login')
    
   return render(request, 'login.html')


def logout(request):
    request.session.clear()
    return redirect('home')