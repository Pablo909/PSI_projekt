from django.db import models


class Klient(models.Model):
    idBilet = models.IntegerField(primary_key=True, null=False)
    kwota = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    numerTelefonu = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    haslo = models.CharField(max_length=45)


class Miejsce(models.Model):
    idMiejsce= models.IntegerField(primary_key=True, null=False)
    sektor = models.CharField(max_length=10)
    rzad = models.IntegerField()
    numer = models.IntegerField()


class Druzyna(models.Model):
    idDruzyna = models.IntegerField(primary_key=True, null=False)
    nazwa = models.CharField(max_length=45)


class Mecz(models.Model):
    idMecz = models.IntegerField(primary_key=True, null=False)
    data = models.DateTimeField()
    idDruzyna1 = models.ForeignKey(Druzyna, on_delete=models.CASCADE, related_name="Team1")
    idDruzyna2 = models.ForeignKey(Druzyna, on_delete=models.CASCADE, related_name="Team2")


class Bilet(models.Model):
    idBilet = models.IntegerField(primary_key=True, null=False)
    kwota = models.FloatField()
    idKlient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    idMecz = models.ForeignKey(Mecz, on_delete=models.CASCADE)
    idMiejsce = models.ForeignKey(Miejsce, on_delete=models.CASCADE)


