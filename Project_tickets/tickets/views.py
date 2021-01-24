from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Place, Team, Match, Ticket
from .serializers import ClientSerializer, PlaceSerializer, TeamSerializer, MatchSerializer, TicketSerializer
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# Create your views here.


def default(request):
    return HttpResponse("<h1>Witaj w mojej aplikacji</h1>")


class ClientView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name = 'client-list'
    filter_fields = ['second_name', 'first_name']
    search_fields = ['second_name', 'first_name', 'email', 'phone_number']
    ordering_fields = ['second_name', 'first_name']


class ClientDetails(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name = 'client-detail'


class PlaceView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    name = 'place-list'
    filter_fields = ['sector', 'row', 'number']
    search_fields = ['sector', 'row', 'number']
    ordering_fields = ['sector', 'row', 'number']


class PlaceDetails(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    name = 'place-detail'


class TeamView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    name = 'team-list'
    filter_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']


class TeamDetails(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    name = 'team-detail'


class MatchView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    name = 'match-list'
    filter_fields = ['date', 'id_team1', 'id_team2']
    search_fields = ['date', 'id_team1__name', 'id_team2__name']
    ordering_fields = ['date', 'id_team1', 'id_team2']


class MatchDetails(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    name = 'match-detail'


class TicketView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    name = 'ticket-view'
    filter_fields = ['price', 'id_match', 'id_client']
    search_fields = ['price', 'id_match__date', 'id_client__second_name', 'id_client__first_name']
    ordering_fields = ['price', 'id_match', 'id_client']


class TicketDetails(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    name = 'ticket-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'Client': reverse(ClientView.name, request=request),
                         'Place': reverse(PlaceView.name, request=request),
                         'Team': reverse(TeamView.name, request=request),
                         'Match': reverse(MatchView.name, request=request),
                         'Ticket': reverse(TicketView.name, request=request),
                         })

