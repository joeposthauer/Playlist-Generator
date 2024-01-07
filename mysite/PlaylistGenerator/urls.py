from django.urls import path

from . import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path("parameters/", views.parameters, name="parameters"),
    path("callback/", views.callback, name="callback")
]