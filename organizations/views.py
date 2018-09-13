from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from users.decorators import admin_required
from .forms import CreateForm
from .models import Organization
# from .utils import render_to_pdf
from ticket_ms.utils import render_pdf
# Create your views here.


@login_required
def listview(request):

    output = request.GET.get("output", "")

    queryset_list = Organization.objects.all()

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(name__icontains=query) |
            Q(address__icontains=query) |
            Q(contact_person1__icontains=query) |
            Q(contact_person2__icontains=query)
        ).distinct()

    paginator = Paginator(queryset_list, 10)

    page = request.GET.get('page')

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        'object_list' : queryset,
        'object_pdf_list' : queryset_list,
    }

    if output == "pdf":
        return render_pdf('organizations/list_pdf.html', context, filename='org.pdf')

    return render(request, 'organizations/list.html', context)


@login_required
@admin_required
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


@login_required
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


@login_required
@admin_required
def deleteview(request, id=None):
    instance = get_object_or_404(Organization, id=id)
    instance.delete()
    return redirect('organizations:list')


@login_required
def detailview(request, id=None):
    object = get_object_or_404(Organization, id=id)
    return render(request, 'organizations/detail.html', {'object': object})


# @login_required
# def pdf_generate_view(request, *args, **kwargs):
#     queryset = Organization.objects.all()
#     template = get_template('organizations/org_list_pdf.html')
#     context = {
#         'object_list': queryset,
#         'base_url': 'http://localhost:8000'
#     }
#     html = template.render(context)
#     pdf = render_to_pdf('organizations/org_list_pdf.html', context)
#     # return HttpResponse(pdf, content_type='application/pdf')
#     return pdf

