from django.shortcuts import render, redirect
from .models import  User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect("/")       
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('register_email')
        birth=request.POST.get('date_of_birth')
        password=request.POST.get('register_password')
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        logged_user= User.objects.create(first_name=first_name, last_name=last_name, email=email, date_of_birth= birth, password= pw_hash)
        request.session['id'] = logged_user.id
        print(logged_user)
        return redirect("/books")
    else:
        if "logged_user.id" not in request.session:
            return redirect("/")
    return redirect("/")
        
def login(request):
    if request.method == 'POST':
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect("/")
        email=request.POST.get('login_email')
        user = User.objects.filter(email = email)
        if len(user) == 1:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['login_password'].encode(), logged_user.password.encode()):
                request.session['id'] = logged_user.id
                return redirect("/books")
    return redirect("/")

def users(request, id):
    user = User.objects.filter(id=id)
    if user:
        logged_user= user[0]
        context={
            'user':logged_user
        }
    return render(request, 'users.html', context)

def logout(request):
    request.session.clear()
    return redirect("/")