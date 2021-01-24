# \myclub_root\events\urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    path('client/', views.ClientView.as_view(), name=views.ClientView.name),
    path('client/<int:pk>', views.ClientDetails.as_view(), name=views.ClientDetails.name),
    path('place/', views.PlaceView.as_view(), name=views.PlaceView.name),
    path('place/<int:pk>', views.PlaceDetails.as_view(), name=views.PlaceDetails.name),
    path('team/', views.TeamView.as_view(), name=views.TeamView.name),
    path('team/<int:pk>', views.TeamDetails.as_view(), name=views.TeamDetails.name),
    path('match/', views.MatchView.as_view(), name=views.MatchView.name),
    path('match/<int:pk>', views.MatchDetails.as_view(), name=views.MatchDetails.name),
    path('ticket/', views.TicketView.as_view(), name=views.TicketView.name),
    path('ticket/<int:pk>', views.TicketDetails.as_view(), name=views.TicketDetails.name),
    path('user/', views.UserView.as_view(), name=views.UserView.name),
    path('user/<int:pk>', views.UserDetails.as_view(), name=views.UserDetails.name),
]