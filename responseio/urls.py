from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("get-answer", views.get_answer, name="get-answer")
]
