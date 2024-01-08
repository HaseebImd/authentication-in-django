from django.shortcuts import render
from django.contrib import messages
from .models import CustomUser  # Import your CustomUser model
from django.contrib.auth import authenticate


def signup(request):
    if request.method == "GET":
        return render(request, "signup.html")
    elif request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        existing_user = CustomUser.objects.filter(username=username)
        if existing_user.exists():
            messages.info(request, "User with this username already exists")
            return render(request, "signup.html")

        existing_email = CustomUser.objects.filter(email=email)
        if existing_email.exists():
            messages.info(request, "User with this email already exists")
            return render(request, "signup.html")

        # Create user and set password
        new_user = CustomUser.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
        )
        new_user.set_password(password)
        new_user.save()

        messages.success(request, "Account created successfully")
        return render(request, "signup.html")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username, password)
        if user:
            messages.info(request, "Welcome to Dashboard")
            login(user)
            return render(request, "dashboard.html")
        else:
            messages.error(request, "Username or Password is incorrect")
            return render(request, "login.html")
