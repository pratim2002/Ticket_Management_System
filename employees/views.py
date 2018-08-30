from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from users.models import USER_ROLES, User
from .models import Employee
from .forms import CreateForm
# Create your views here.

@login_required
def listview(request):
    employee = Employee.objects.first()
    emp_count = Employee.objects.count()
    if emp_count == 0:
        return HttpResponseRedirect('/employees/add/')
    else:
        return redirect(reverse('employees:detail', kwargs={'id': employee.pk}))

@login_required
def createview(request):
    form = CreateForm(request.POST, request.FILES)
    errors = None
    if form.is_valid():
        instance = form.save(commit=False)
        user = User()
        user.first_name = instance.first_name
        user.last_name = instance.last_name
        user.email = instance.email
        user.username = instance.email
        user.set_password("{}{}".format(instance.first_name,'@Zeftware'))
        user.role = USER_ROLES.employee
        user.save()
        instance.save()
        return HttpResponseRedirect('/employees/')
    if form.errors:
        errors = form.errors

    template_name = 'employees/forms.html'
    context = {
        'form' : form,
        'errors' : errors
    }
    return render(request, template_name, context)

@login_required
def editview(request, id=None):
    instance = get_object_or_404(Employee, id=id)
    form = CreateForm(request.POST or None, request.FILES or None, instance=instance)
    errors = None
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect('/employees/')
    if form.errors:
        errors = form.errors

    template_name = 'employees/form.html'
    context = {
        'form' : form,
        'errors' : errors
    }
    return render(request, template_name, context)

@login_required
def deleteview(request, id=None):
    instance = get_object_or_404(Employee, id=id)
    instance.delete()
    return redirect('employees:list')

@login_required
def detailview(request, id=None):
    employees = Employee.objects.all()
    employee = get_object_or_404(Employee, id=id)
    context = {
        'employees': employees,
        'employee' : employee
    }
    return render(request, 'employees/detail.html', context)