# Generated by Django 3.1.3 on 2020-12-07 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('idMatch', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('idTicket', models.IntegerField(primary_key=True, serialize=False)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='mecz',
            name='idDruzyna1',
        ),
        migrations.RemoveField(
            model_name='mecz',
            name='idDruzyna2',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='kwota',
            new_name='firstName',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='idBilet',
            new_name='idClient',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='haslo',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='numerTelefonu',
            new_name='phoneNumber',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='nazwisko',
            new_name='secondName',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='idMiejsce',
            new_name='idPlace',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='numer',
            new_name='number',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='rzad',
            new_name='row',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='sektor',
            new_name='sector',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='idDruzyna',
            new_name='idTeam',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='nazwa',
            new_name='name',
        ),
        migrations.RenameModel(
            old_name='Klient',
            new_name='Client',
        ),
        migrations.RenameModel(
            old_name='Miejsce',
            new_name='Place',
        ),
        migrations.RenameModel(
            old_name='Druzyna',
            new_name='Team',
        ),
        migrations.DeleteModel(
            name='Bilet',
        ),
        migrations.DeleteModel(
            name='Mecz',
        ),
        migrations.AddField(
            model_name='ticket',
            name='idClient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.client'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='idMatch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.match'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='idPlace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.place'),
        ),
        migrations.AddField(
            model_name='match',
            name='idTeam1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Team1', to='tickets.team'),
        ),
        migrations.AddField(
            model_name='match',
            name='idTeam2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Team2', to='tickets.team'),
        ),
    ]
