from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .api import get_response
from .forms import PublicKeyForm, TypeForm


class StartView(FormView):
    form_class = PublicKeyForm
    template_name = 'web_app/start.html'


class FilesView(TemplateView, FormView):
    template_name = 'web_app/files.html'
    form_class = TypeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['files'] = get_response(self.request.GET['key'], self.request.GET['path'])  # добавляем в контекст
        # переменную, хранящую список, полученный из ф-ции get_response. Арг. ф-ции служат переменные, полученные из
        # формы.
        context['key'] = self.request.GET['key']    # переменная из формы
        context['path'] = self.request.GET['path']  # переменная из формы
        context['type'] = self.request.GET.get('type', TypeForm.ALL)
        return context