from rest_framework import serializers
from .models import Client, Place, Team, Match, Ticket


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'url', 'first_name', 'second_name', 'phone_number', 'email']


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'url', 'sector', 'row', 'number']


class TeamSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Team
        fields = ['id', 'url', 'name']


class MatchSerializer(serializers.HyperlinkedModelSerializer):
    id_team1 = serializers.SlugRelatedField(queryset=Team.objects.all(), slug_field='name')
    id_team2 = serializers.SlugRelatedField(queryset=Team.objects.all(), slug_field='name')

    class Meta:
        model = Match
        fields = ['id', 'url', 'date', 'id_team1', 'id_team2']


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    id_client = serializers.StringRelatedField()
    id_match = serializers.StringRelatedField()
    id_place = serializers.StringRelatedField()

    class Meta:
        model = Ticket
        fields = ['id', 'url', 'price', 'id_client', 'id_match', 'id_place']
