from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! Please Sign In')
            return redirect('home')

    else:
        form = UserRegisterForm()
    return render(request,'users/register.html', {'form':form})

def signin(request):
    return render(request, 'users/signin.html')

def manage_users(request):
    groups_list = Group.objects.all()
    users_list = User.objects.filter(groups__name__in=['UserAdmin', 'Reader', 'ProjectManager']).distinct()
    return render(request, 'users/users-list.html', {'users_list': users_list, 'groups_list':groups_list})