from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateUser
from hashlib import sha256
from django.contrib.auth.models import User


# Home Page View
def home_page(request):
    return render(request, 'welcome.html')


# Link To Add User If You Are a Admin 
def add_new_user(request):
    return render(request, 'add_user.html')



# Only Admin Can Add User As You Said .
# Form To add User
login_required(login_url='login')
def add_user(request):
    if request.method == 'POST':
        register_form = CreateUser(request.POST)
        if register_form.is_valid():
            
            # Hashing Pass Manually
            # password = register_form.cleaned_data.get('password1')
            # Creating Hash With the Help of Sha 256
            # hash_pass = sha256(password.encode('ascii')).hexdigest()
            # print(password)
            
            # Using inbuild Django Password Hashing Which is also sha256
            register_form.save()
            user = User.objects.get(username = register_form.cleaned_data.get('username'))
            name = user.username
            password = user.password

            # Sending Hash Pass As Context 
            return render(request ,'show_hashed_pass.html', context={
                "user_name": user,
                "hash_pass": password
            })
    else:
        register_form = CreateUser()
    context = {
        "form": register_form
        }
    return render(request, 'create_user.html', context=context)

