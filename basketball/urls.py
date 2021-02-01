from django.urls import path
from basketball import views as basketball_view

urlpatterns = [
    path('basketball/',basketball_view.getBasketballMatches),
    path('basketball/createMatches/',basketball_view.createMatchesFromFile),
    path('basketball/<str:match_id>/',basketball_view.getBasketballMatchFromId),
]