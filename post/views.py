from django.http import HttpResponse
from django.views.generic.edit import FormView

from .forms import SimpleForm


class SimpleFormView(FormView):

    template_name = 'simple_form.html'
    form_class = SimpleForm

    def form_valid(self, form):
        return HttpResponse('Valid POST\n')
