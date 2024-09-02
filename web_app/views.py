from django.views.generic import TemplateView

from .api import get_response



class StartView(TemplateView):
    template_name = 'web_app/start.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['files'] = get_response()
        return context