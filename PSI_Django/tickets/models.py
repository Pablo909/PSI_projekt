from django.db import models


class Client(models.Model):
    idClient = models.IntegerField(primary_key=True, null=False)
    firstName = models.CharField(max_length=45)
    secondName = models.CharField(max_length=45)
    phoneNumber = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)


class Place(models.Model):
    idPlace = models.IntegerField(primary_key=True, null=False)
    sector = models.CharField(max_length=10)
    row = models.IntegerField()
    number = models.IntegerField()


class Team(models.Model):
    idTeam = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=45)


class Match(models.Model):
    idMatch = models.IntegerField(primary_key=True, null=False)
    date = models.DateTimeField()
    idTeam1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="Team1")
    idTeam2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="Team2")


class Ticket(models.Model):
    idTicket = models.IntegerField(primary_key=True, null=False)
    price = models.FloatField()
    idClient = models.ForeignKey(Client, on_delete=models.CASCADE)
    idMatch = models.ForeignKey(Match, on_delete=models.CASCADE)
    idPlace = models.ForeignKey(Place, on_delete=models.CASCADE)


