from django.urls import path
from hockey import views as hockey_view

urlpatterns = [
    path('hockey/',hockey_view.getHockeyMatches),
    path('hockey/createMatches/',hockey_view.createMatchesFromFile),
    path('hockey/<str:match_id>/',hockey_view.getHockeyMatchFromId),
]