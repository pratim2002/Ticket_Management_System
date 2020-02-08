from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
# from yourproject.utils import render_to_pdf  # created in step 4
from .utils import render_to_pdf

# class GeneratePdf(View):
#     def get(self, request, *args, **kwargs):
#         template = get_template('pdf/invoice.html')
#         context = {
#             'organization_id': 'Zeftware',
#             'address': 'Biratnagar',
#             'phone': '021460567',
#         }
#         html = template.render(context)
#         # pdf = render_to_pdf('pdf/invoice.html', data)
#         # return HttpResponse(pdf, content_type='application/pdf')
#         return HttpResponse(html)


def generate_view(request, *args, **kwargs):
    template = get_template('pdf/invoice.html')
    context = {
        'organization_id': 'Zeftware',
        'address': 'Biratnagar',
        'phone': '021460567',
    }
    html = template.render(context)
    pdf = render_to_pdf('pdf/invoice.html', context)
    # return HttpResponse(pdf, content_type='application/pdf')
    return pdf
