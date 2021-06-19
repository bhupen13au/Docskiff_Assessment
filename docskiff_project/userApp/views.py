from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Product


def home(request):
    """
    Redirects to the login page
    """
    return redirect('login')


def register(request):
    """
    View for registration page and posting user submitted data
    """
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm = request.POST['confirm']

        if password == confirm:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already exists')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists')
            else:
                user = User.objects.create_user(email=email, username=username, password=password)
                user.save()
        else:
            messages.info(request, 'password not matching')
            return render(request, 'registration.html')
        return redirect('login')
    else:
        return render(request, 'registration.html')


def login(request):
    """
    View for login page and authenticating user which will redirect to details page
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('/user/details/'+str(username))
        else:
            messages.info(request, 'invalid username/password')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def details(request, username):
    """
    View for logged-in user which shows user owned products
    """
    if request.user.is_authenticated:
        user_products = Product.objects.filter(owner__username=username)
        context = {}
        context['products'] = user_products
        context['username'] = username
        return render(request, 'details.html', context)
    else:
        return redirect('home')


def logout(request):
    """
    View after logout which will redirect to home page
    """
    auth.logout(request)
    return redirect('home')
