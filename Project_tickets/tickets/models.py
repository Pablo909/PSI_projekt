from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.


class Client(models.Model):
    first_name = models.CharField(max_length=45, null=False)
    second_name = models.CharField(max_length=45, null=False)
    phone_number = models.CharField(max_length=12, unique=True)
    email = models.CharField(max_length=45, unique=True, null=False)

    class Meta:
        ordering = ('second_name', 'first_name')

    def __str__(self):
        return self.first_name+' '+self.second_name


class Place(models.Model):
    sector = models.CharField(max_length=10, null=False)
    row = models.IntegerField(null=False)
    number = models.IntegerField(null=False)

    class Meta:
        ordering = ('sector', 'row', 'number')

    def __str__(self):
        return self.sector+' '+str(self.row)+' '+str(self.number)


class Team(models.Model):
    name = models.CharField(max_length=45, null=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Match(models.Model):
    date = models.DateTimeField(null=False)
    id_team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="home", null=False)
    id_team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="away", null=False)

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return str(self.date)+' '+str(self.id_team1)+'-'+str(self.id_team2)


class Ticket(models.Model):
    price = models.FloatField(null=False, validators=[MinValueValidator(0)])
    id_client = models.ForeignKey(Client, null=True, blank=True, on_delete=models.SET_NULL, related_name="client_tickets")
    id_match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name="match_tickets", null=False)
    id_place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="place_tickets", null=False)

    class Meta:
        ordering = ('id_match', 'id_place')

    def __str__(self):
        return str(self.id_match) + ", place: " + str(self.id_place) + ", client: " + str(self.id_client) + ", price: " \
               + str(self.price) + "zł"
