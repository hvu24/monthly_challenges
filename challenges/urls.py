from django.urls import path
from . import views

urlpatterns = [
    # path('january', views.january),
    # path('february', views.february),
    # path('march', views.march),
    path("", views.index), #/challenges
    path('<int:month>', views.monthly_challenge_by_number), ##check for integer has to go before checking string
    path('<str:month>', views.monthly_challenge, name='month-challenge') ##dynamic path, month can be anything
]
