from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .api import get_response
from .forms import PublicKeyForm


class StartView(FormView):
    form_class = PublicKeyForm
    template_name = 'web_app/start.html'

class FilesView(TemplateView):
    template_name = 'web_app/files.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['files'] = get_response(self.request.GET['key'])
        return context