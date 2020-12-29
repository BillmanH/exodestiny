from django.urls import path

from . import views

urlpatterns = [path("control", views.control), path("solarsystem", views.solarsystem)]
