from django.db import models

# Create your models here.


class Client(models.Model):
    id_client = models.IntegerField(primary_key=True, null=False)
    first_name = models.CharField(max_length=45)
    second_name = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    def __str__(self):
        return self.first_name+' '+self.second_name


class Place(models.Model):
    id_place = models.IntegerField(primary_key=True, null=False)
    sector = models.CharField(max_length=10)
    row = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return self.sector+' '+str(self.row)+' '+str(self.number)


class Team(models.Model):
    id_team = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class Match(models.Model):
    id_match = models.IntegerField(primary_key=True, null=False)
    date = models.DateTimeField()
    id_team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="Team1")
    id_team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="Team2")

    def __str__(self):
        return self.date


class Ticket(models.Model):
    id_ticket = models.IntegerField(primary_key=True, null=False)
    price = models.FloatField()
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_match = models.ForeignKey(Match, on_delete=models.CASCADE)
    id_place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return self.price
