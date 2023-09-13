from django.urls import path

from . import views

urlpatterns = [
    #polls/
    path("", views.index, name="index"),
    #polls/int
    path("<int:question_id>", views.detail, name="detail"),
    #polls/int/vote
    path("<int:question_id>/vote", views.vote, name="vote"),
    #polls/int/results
    path("<int:question_id>/results", views.results, name="results"),
]