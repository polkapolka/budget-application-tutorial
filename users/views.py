from django.contrib import messages
from django.shortcuts import render, redirect,render_to_response
from django.urls import reverse
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.models import User, Group
from .forms import UserRegisterForm
import json
import os




def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=form.cleaned_data.get('username'))
            user.groups.add(form.group)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! Please Sign In')
            return redirect('home')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def signin(request):
    return render(request, 'users/signin.html')


def manage_users(request):
    if request.method == 'GET':
        form = UserRegisterForm()
        groups_list = Group.objects.all()
        users_list = User.objects.filter(groups__name__in=['UserAdmin', 'Reader', 'ProjectManager']).distinct()
        return render(request, 'users/users-list.html',
                      {'users_list': users_list, 'form': form, 'groups_list': groups_list})
    elif request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            user.groups.add(Group.objects.get(name=form.data.get('group')))
            messages.success(request, f'Account created for {username}!')
            return redirect('users-list')
        else:
            messages.warning(request, f'No account created.')
            return redirect('users-list')
    elif request.method == 'DELETE':
        try:
            id = json.loads(request.body)['id']
            user = User.objects.get(id=id)
            user.delete()
        except:
            return HttpResponse(status=404)
        return HttpResponse(status=204)
