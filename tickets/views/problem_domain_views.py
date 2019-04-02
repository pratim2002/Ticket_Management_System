from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from tickets.forms import CreateProblemForm
from tickets.models import ProblemDomain
from users.decorators import admin_required


@login_required
def problem_listview(request):
    queryset = ProblemDomain.objects.all()
    context = {
        'problem_list': queryset
    }
    template_name = 'tickets/problem_list.html'
    return render(request, template_name, context)


@admin_required
@login_required
def problem_create_view(request):
    form = CreateProblemForm(request.POST or None)
    errors = None
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Problem domain added.")
        return redirect('tickets:problem_list')
    if form.errors:
        errors = form.errors

    template_name = 'tickets/problem_forms.html'
    context = {
        'form': form,
        'errors': errors
    }
    return render(request, template_name, context)


@admin_required
@login_required
def problem_edit_view(request, id=None):
    instance = get_object_or_404(ProblemDomain, id=id)
    form = CreateProblemForm(request.POST or None, instance=instance)
    errors = None
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Problem domain edited.")
        return redirect(reverse('tickets:problem_list'))
    if form.errors:
        errors = form.errors

    template_name = 'tickets/problem_edit.html'
    context = {"form": form, "errors": errors}
    return render(request, template_name, context)


@admin_required
@login_required
def problem_delete_view(request, id=None):
    instance = get_object_or_404(ProblemDomain, id=id)
    instance.delete()
    messages.info(request, "Problem domain deleted.")
    return redirect('tickets:problem_list')
