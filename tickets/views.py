from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from ticket_ms import settings
from users.decorators import admin_required
from .models import Ticket
from .forms import CreateForm


# Create your views here.

@login_required
def listview(request):
    queryset = Ticket.objects.all()

    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(
            Q(ticket_type__icontains=query) |
            Q(status__icontains=query)
        )

    template1 = 'tickets/list.html'
    template2 = 'tickets/ticket_for_emp.html'
    context = {
        'object_list': queryset
    }
    if request.user.is_admin():
        return render(request, template1, context)

    return render(request, template2, context)


@login_required
def createview(request):
    form = CreateForm(request.POST, request.FILES)
    errors = None
    if form.is_valid():
        instance = form.save(commit=False)
        email_id = instance.employee_id.email

        instance.save()

        subject = 'Mail Testing'
        message = 'Zeftware Solutions Generate Tickets for you. Please login and see the ticket.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email_id]

        send_mail(subject, message, email_from, recipient_list, fail_silently=False)

        return HttpResponseRedirect("/tickets/")
    if form.errors:
        errors = form.errors

    template_name = 'tickets/forms.html'
    context = {
        "form": form,
        "errors": errors
    }
    return render(request, template_name, context)


@login_required
def editview(request, id=None):
    instance = get_object_or_404(Ticket, id=id)
    form = CreateForm(request.POST or None, request.FILES or None, instance=instance)
    errors = None
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/tickets/")
    if form.errors:
        errors = form.errors

    template_name = 'tickets/form.html'
    context = {"form": form, "errors": errors}
    return render(request, template_name, context)


@login_required
@admin_required
def deleteview(request, id=None):
    instance = get_object_or_404(Ticket, id=id)
    instance.delete()
    return redirect('tickets:list')


@login_required
def detailview(request, id=None):
    object = get_object_or_404(Ticket, id=id)
    return render(request, 'tickets/detail.html', {'object': object})
