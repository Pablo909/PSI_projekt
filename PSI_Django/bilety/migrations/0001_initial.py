# Generated by Django 3.1.3 on 2020-11-23 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Druzyna',
            fields=[
                ('idDruzyna', models.IntegerField(primary_key=True, serialize=False)),
                ('nazwa', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Klient',
            fields=[
                ('idBilet', models.IntegerField(primary_key=True, serialize=False)),
                ('kwota', models.CharField(max_length=45)),
                ('nazwisko', models.CharField(max_length=45)),
                ('numerTelefonu', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('haslo', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Miejsce',
            fields=[
                ('idMiejsce', models.IntegerField(primary_key=True, serialize=False)),
                ('sektor', models.CharField(max_length=10)),
                ('rzad', models.IntegerField()),
                ('numer', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mecz',
            fields=[
                ('idMecz', models.IntegerField(primary_key=True, serialize=False)),
                ('data', models.DateTimeField()),
                ('idDruzyna1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Team1', to='bilety.druzyna')),
                ('idDruzyna2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Team2', to='bilety.druzyna')),
            ],
        ),
        migrations.CreateModel(
            name='Bilet',
            fields=[
                ('idBilet', models.IntegerField(primary_key=True, serialize=False)),
                ('kwota', models.FloatField()),
                ('idKlient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bilety.klient')),
                ('idMecz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bilety.mecz')),
                ('idMiejsce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bilety.miejsce')),
            ],
        ),
    ]