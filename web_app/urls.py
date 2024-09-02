from django.urls import path
from . import views

urlpatterns = [
    path('', views.StartView.as_view()),
    path('files/', views.FilesView.as_view()),
]