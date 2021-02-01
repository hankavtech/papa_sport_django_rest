from django.urls import path
from cricket import views as cricket_view

urlpatterns = [
    path('cricket/',cricket_view.getCricketMatches),
    path('cricket/createMatches/',cricket_view.createMatchesFromFile),
    path('cricket/<str:match_id>/',cricket_view.getCricketMatchFromId),
]