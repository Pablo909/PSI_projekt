from rest_framework import serializers
from .models import Client, Place, Team, Match, Ticket


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id_client', 'first_name', 'second_name', 'phone_number', 'email', 'password']


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id_place', 'sector', 'row', 'number']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id_team', 'name']


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['id_match', 'date', 'id_team1', 'id_team2']


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id_ticket', 'price', 'id_client', 'id_match', 'id_place']
