from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProjectView.as_view()),
    path('headers/', views.get_headers),
]
