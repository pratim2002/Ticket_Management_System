from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from tickets.forms import CreateBranchForm
from tickets.models import Branch
from users.decorators import admin_required


@login_required
def branch_listview(request):
    queryset = Branch.objects.all()
    context = {
        'branch_list': queryset
    }
    template_name = 'tickets/branch_list.html'
    return render(request, template_name, context)


@admin_required
@login_required
def branch_create_view(request):
    form = CreateBranchForm(request.POST or None)
    errors = None
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Branch added.")
        return redirect('tickets:branch_list')
    if form.errors:
        errors = form.errors

    template_name = 'tickets/branch_forms.html'
    context = {
        'form': form,
        'errors': errors
    }
    return render(request, template_name, context)


@admin_required
@login_required
def branch_edit_view(request, id=None):
    instance = get_object_or_404(Branch, id=id)
    form = CreateBranchForm(request.POST or None, instance=instance)
    errors = None
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Branch edited.")
        return redirect(reverse('tickets:branch_list'))
    if form.errors:
        errors = form.errors

    template_name = 'tickets/branch_edit.html'
    context = {"form": form, "errors": errors}
    return render(request, template_name, context)


@admin_required
@login_required
def branch_delete_view(request, id=None):
    instance = get_object_or_404(Branch, id=id)
    instance.delete()
    messages.info(request, "Branch deleted.")
    return redirect('tickets:branch_list')
