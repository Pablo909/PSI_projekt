# Generated by Django 3.1.3 on 2020-12-14 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='firstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='idClient',
            new_name='id_client',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='phoneNumber',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='secondName',
            new_name='second_name',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='idMatch',
            new_name='id_match',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='idTeam1',
            new_name='id_team1',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='idTeam2',
            new_name='id_team2',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='idPlace',
            new_name='id_place',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='idTeam',
            new_name='id_team',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='idClient',
            new_name='id_client',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='idMatch',
            new_name='id_match',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='idPlace',
            new_name='id_place',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='idTicket',
            new_name='id_ticket',
        ),
    ]