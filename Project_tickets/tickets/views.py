from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Place, Team, Match, Ticket
from .serializers import ClientSerializer, PlaceSerializer, TeamSerializer, MatchSerializer, TicketSerializer, \
    UserSerializer
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet, CharFilter
from django.contrib.auth.models import User
from rest_framework import permissions
# Create your views here.


def default(request):
    return HttpResponse("<h1>Witaj w mojej aplikacji</h1>")


class ClientView(generics.ListCreateAPIView):
    #permission_classes = [permissions.IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name = 'client-list'
    filterset_fields = ['second_name', 'first_name']
    search_fields = ['second_name', 'first_name', 'email', 'phone_number']
    ordering_fields = ['second_name', 'first_name']


class ClientDetails(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [permissions.IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name = 'client-detail'


class PlaceView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    name = 'place-list'
    filterset_fields = ['sector', 'row', 'number']
    search_fields = ['sector', 'row', 'number']
    ordering_fields = ['sector', 'row', 'number']


class PlaceDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    name = 'place-detail'


class TeamView(generics.ListCreateAPIView):
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    name = 'team-list'
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']


class TeamDetails(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    name = 'team-detail'


class MatchFilter(FilterSet):
    id_team1__name = CharFilter(field_name='id_team1__name')
    id_team2__name = CharFilter(field_name='id_team2__name')
    from_date = DateTimeFilter(field_name='date', lookup_expr='gte')
    to_date = DateTimeFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = Match
        fields = ['id_team1__name', 'id_team2__name', 'from_date', 'to_date']


class MatchView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    name = 'match-list'
    filterset_class = MatchFilter
    search_fields = ['date', 'id_team1__name', 'id_team2__name']
    ordering_fields = ['date', 'id_team1', 'id_team2']


class MatchDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    name = 'match-detail'


class TicketFilter(FilterSet):
    from_price = NumberFilter(field_name='price', lookup_expr='gte')
    to_price = NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Ticket
        fields = ['from_price', 'to_price']


class TicketView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    name = 'ticket-list'
    filterset_class = TicketFilter
    search_fields = ['price', 'id_match__date', 'id_match__id_team1__name', 'id_match__id_team2__name',
                     'id_client__second_name', 'id_client__first_name']
    ordering_fields = ['price', 'id_match', 'id_client']


class TicketDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    name = 'ticket-detail'


class UserView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'


class UserDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'Client': reverse(ClientView.name, request=request),
                         'Place': reverse(PlaceView.name, request=request),
                         'Team': reverse(TeamView.name, request=request),
                         'Match': reverse(MatchView.name, request=request),
                         'Ticket': reverse(TicketView.name, request=request),
                         'User': reverse(UserView.name, request=request),
                         })

