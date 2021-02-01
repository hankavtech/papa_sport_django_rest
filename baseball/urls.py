from django.urls import path
from baseball import views as baseball_view

urlpatterns = [
    path('baseball/',baseball_view.getBaseballMatches),
    path('baseball/createMatches/',baseball_view.createMatchesFromFile),
    path('baseball/<str:match_id>/',baseball_view.getBaseballMatchFromId),
]