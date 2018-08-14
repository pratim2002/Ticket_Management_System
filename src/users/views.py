from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import RegisterForm, LoginForm
# Create your views here.

@login_required
def index(request):
    return render(request, 'index.html')

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

    context = { 'form' : form}
    return render(request, 'users/register.html', context  )

def user_login(request):
    """
    Login a user
    """
    next = request.GET.get('next', None)
    # if request.user.is_authenticated():
    #     return redirect('index')

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
                return render(request, 'users/login.html', context)
            else:
                login(request, user)
                if next:
                    return redirect(next)
                return redirect('users:index')

    return render(request, 'users/login.html', context)

def user_logout(request):
    """
    Logout a user
    """
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('users:login')
