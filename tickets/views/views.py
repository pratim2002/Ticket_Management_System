from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from ticket_ms import settings
from tickets.filters import TicketFilter
from users.decorators import admin_required
from tickets.models import Ticket, Branch
from tickets.forms import CreateForm


# Create your views here.

@login_required
def listview(request):
    # source_filter = request.GET.get('source')
    # status_filter = request.GET.get('status')
    # if source_filter or status_filter:
    #     query = Ticket.objects.filter(source=source_filter) or Ticket.objects.filter(status=status_filter)
    #     context = {
    #         'object_list': query,
    #         'source_filter': source_filter,
    #         'status_filter': status_filter,
    #     }
    #
    # else:
    #     query = Ticket.objects.all()
    #     context = {
    #         'object_list': query,
    #     }

    query = Ticket.objects.all()
    ticket_filter = TicketFilter(request.GET, queryset=query)
    context = {
        'filter': ticket_filter
    }
    template = 'tickets/list.html'
    return render(request, template, context)



@login_required
def createview(request):
    form = CreateForm(request.POST, request.FILES)
    errors = None
    if form.is_valid():
        instance = form.save(commit=False)
        email_id = instance.employee_id.email
        instance.save()
        messages.success(request, "Record added.")

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
        messages.success(request, "Record edited.")
        return HttpResponseRedirect("/tickets/")
    if form.errors:
        errors = form.errors

    template_name = 'tickets/form.html'
    context = {"form": form, "errors": errors}
    return render(request, template_name, context)


@admin_required
@login_required
def deleteview(request, id=None):
    instance = get_object_or_404(Ticket, id=id)
    instance.delete()
    messages.info(request, "Record deleted.")
    return redirect('tickets:list')
