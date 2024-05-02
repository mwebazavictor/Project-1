from django.urls import path
from . import views

urlpatterns = [
    path("flights/index", views.index, name="index")
]