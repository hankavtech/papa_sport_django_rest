from django.urls import path
from football import views as football_view

urlpatterns = [
    path('soccer/',football_view.getFootballMatches),
    path('soccer/createMatches/',football_view.createMatchesFromFile),
    path('soccer/<str:match_id>/',football_view.getFootballMatchFromId),
]
