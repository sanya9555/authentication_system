from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Registration view
def register(request):
    if request.method=="GET":
        try:
            return render(request,"register.html")
        except Exception as e:
            print(e)
            return render(request,"notFound.html")
    if request.method=="POST":
        try:
            name=request.POST['name']
            password=request.POST['password']
            email=request.POST['email']          
            user = user.objects.create_user(name,email,password)
            user.save()
            print("Registered sucessfully")
            return render(request,"register.html")
        except Exception as e:
            print(e)
            return render(request,"notFound.html")


    return render(request,"notFound.html")

def login(request):
    if request.method=="GET":
        try:
            return render(request,"login.html")
        except Exception as e:
            print(e)
            return render(request,"notFound.html")
    if request.method == "POST":
        try:
            name = request.POST['name']
            password = request.POST['password']
            user = authenticate(request, username=name, password=password)
            user.save()
            if user is not None:
                login(request,login.html)
                print("Logged in successfully")
                return redirect('/home')
            else:
                print(request, 'Invalid username or password')
                print("Invalid credentials")
        except Exception as e:
            print(e)
            print(request, 'An error occurred during login')
    
    return render(request, 'notFound.html')

@login_required
def home_view(request):
    return render(request, 'home.html')

