from django.db import models

# Create your models here.


class Client(models.Model):
    first_name = models.CharField(max_length=45)
    second_name = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=45)
    email = models.CharField(max_length=45)

    class Meta:
        ordering = ('second_name', 'first_name')

    def __str__(self):
        return self.first_name+' '+self.second_name


class Place(models.Model):
    sector = models.CharField(max_length=10)
    row = models.IntegerField()
    number = models.IntegerField()

    class Meta:
        ordering = ('sector', 'row', 'number')

    def __str__(self):
        return self.sector+' '+str(self.row)+' '+str(self.number)


class Team(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Match(models.Model):
    date = models.DateTimeField()
    id_team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team1")
    id_team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team2")

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return str(self.date)+' '+str(self.id_team1)+'-'+str(self.id_team2)


class Ticket(models.Model):
    price = models.FloatField()
    id_client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL, related_name="client_ticket")
    id_match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name="match_ticket")
    id_place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="place_ticket")

    class Meta:
        ordering = ('id_match', 'id_place')

    def __str__(self):
        return str(self.price)
