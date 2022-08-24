from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.polls_list, name="list"),
    path('<question_text>', views.polls_details, name="details"),
    path('<question_text>/results/', views.polls_results, name="results"),
    path('<question_text>/vote/', views.polls_vote, name="vote")
]
