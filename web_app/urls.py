from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    path('', views.StartView.as_view()),
    path('files/', cache_page(120)(views.FilesView.as_view()), name='files'),
]