from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect

from .forms import CreateForm
from .models import Organization
# Create your views here.

def listview(request):
    queryset = Organization.objects.all()
    context = {
        'object_list' : queryset
    }
    return render(request, 'organizations/list.html', context)

def createview(request):
    form = CreateForm(request.POST, request.FILES)
    errors = None
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/organizations/")
    if form.errors:
        errors = form.errors

    template_name = 'organizations/forms.html'
    context = {"form" : form, "errors" : errors}
    return render(request, template_name, context)

def editview(request, id=None):
    instance = get_object_or_404(Organization, id=id)
    form = CreateForm(request.POST or None, request.FILES or None, instance=instance)
    errors = None
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/organizations/")
    if form.errors:
        errors = form.errors

    template_name = 'organizations/form.html'
    context = {"form": form, "errors": errors}
    return render(request, template_name, context)

def deleteview(request, id=None):
    instance = get_object_or_404(Organization, id=id)
    instance.delete()
    return redirect('organizations:list')

def detailview(request, id=None):
    object = get_object_or_404(Organization, id=id)
    return render(request, 'organizations/detail.html', {'object': object})

