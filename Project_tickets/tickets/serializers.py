from rest_framework import serializers
from .models import Client, Place, Team, Match, Ticket
from django.contrib.auth.models import User


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    client_tickets = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='ticket-detail')

    class Meta:
        model = Client
        fields = ['id', 'url', 'first_name', 'second_name', 'phone_number', 'email', 'client_tickets']


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    place_tickets = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='ticket-detail')

    class Meta:
        model = Place
        fields = ['id', 'url', 'sector', 'row', 'number', 'place_tickets']


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    home = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='match-detail')
    away = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='match-detail')

    class Meta:
        model = Team
        fields = ['id', 'url', 'name', 'home', 'away']


class MatchSerializer(serializers.HyperlinkedModelSerializer):
    id_team1 = serializers.SlugRelatedField(queryset=Team.objects.all(), slug_field='name')
    id_team2 = serializers.SlugRelatedField(queryset=Team.objects.all(), slug_field='name')
    match_tickets = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='ticket-detail')

    class Meta:
        model = Match
        fields = ['id', 'url', 'date', 'id_team1', 'id_team2', 'match_tickets']


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    id_client = serializers.StringRelatedField()
    id_match = serializers.StringRelatedField()
    id_place = serializers.StringRelatedField()

    class Meta:
        model = Ticket
        fields = ['id', 'url', 'price', 'id_client', 'id_match', 'id_place']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'password', 'email']
