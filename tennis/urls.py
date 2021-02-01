from django.urls import path
from tennis import views as tennis_view

urlpatterns = [
    path('tennis/',tennis_view.getTennisMatches),
    path('tennis/createMatches/',tennis_view.createMatchesFromFile),
    path('tennis/<str:match_id>/',tennis_view.getTennisMatchFromId),
]