from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from users.decorators import admin_required
from .forms import RegisterForm, LoginForm, PasswordChangeForm, CreateForm
from .models import User
# Create your views here.


@login_required
def index(request):
    user = request.user
    template = 'users/login.html'

    if user.is_anonymous:
        template = 'users/login.html'
    elif user.is_admin():
        template = 'index.html'
    elif user.is_employee():
        template = 'employee_dashboard.html'
    return render(request, template, {})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('users:index')

    else:
        form = RegisterForm()

    context = {'form': form}
    templates = 'users/register.html'
    return render(request, templates, context)


def user_login(request):
    """
    Login a user
    """
    next = request.GET.get('next', None)
    if request.user.is_authenticated:
        return redirect('users:index')

    form = LoginForm(data=request.POST or None)

    context = {
        'form': form,
    }

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is None:
                messages.error(request, "Invalid login credentials")
                templates = 'users/login.html'
                return render(request, templates, context)
            else:
                login(request, user)
                if next:
                    return redirect(next)
                messages.success(request, 'Successfully logged in!')
                return redirect('users:index')
    templates = 'users/login.html'
    return render(request, templates, context)


@login_required
def user_password_change(request):
    """
    Change user password
    """
    form = PasswordChangeForm(data=request.POST or None, user=request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Password changed successfully")
            return redirect('users:index')

    context = {
        'form': form
    }
    templates = 'users/change_password.html'
    return render(request, templates, context)


def user_logout(request):
    """
    Logout a user
    """
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('users:login')


@login_required
@admin_required
def user_listview(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    templates = 'users/user_list.html'
    return render(request, templates, context)


@login_required
@admin_required
def user_editview(request, id=None):
    instance = get_object_or_404(User, id=id)
    form = CreateForm(request.POST or None, instance=instance)
    errors = None
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "User edited.")
        return HttpResponseRedirect('/users/')
    if form.errors:
        errors = form.errors

    template_name = 'users/form.html'
    context = {"form": form, "errors": errors}
    return render(request, template_name, context)


@login_required
@admin_required
def user_deleteview(request, id=None):
    instance = get_object_or_404(User, id=id)
    instance.delete()
    messages.info(request, "User deleted.")
    return redirect('users:list')


@login_required
@admin_required
def user_createview(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.info(request, "User added.")
            return redirect('users:list')

    else:
        form = RegisterForm()

    context = {'form': form}
    templates = 'users/forms.html'
    return render(request, templates, context)


# @login_required
# @admin_required
# def users_pass_change(request, id=None):
#     instance = get_object_or_404(User, id=id)
#     form = PasswordChangeForm(data=request.POST or None, instance=instance)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('users:list')
#
#     context = {
#         'form': form
#     }
#     return render(request, 'users/users_pass_change.html', context)
