from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .models import Product
from .forms import CreateForm

# Create your views here.
@login_required
def product_listview(request):
    queryset = Product.objects.all()
    context = {
        'object_list' : queryset
    }
    return render(request, 'products/list.html', context)

@login_required
def product_createview(request):
    form = CreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect('/products/')
    if form.errors:
        errors = form.errors

    template_name = 'products/forms.html'
    context = {
        'form': form,
        'errors': errors
    }
    return render(request, template_name, context)

@login_required
def product_editview(request, id=None):
    instance = get_object_or_404(Product, id=id)
    form = CreateForm(request.POST or None, instance=instance)
    errors = None
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/products/")
    if form.errors:
        errors = form.errors

    template_name = 'products/form.html'
    context = {"form": form, "errors": errors}
    return render(request, template_name, context)

@login_required
def product_deleteview(request, id=None):
    instance = get_object_or_404(Product, id=id)
    instance.delete()
    return redirect('products:list')