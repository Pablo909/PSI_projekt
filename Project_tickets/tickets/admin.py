from django.contrib import admin
from .models import Client, Place, Team, Match, Ticket

# Register your models here.

admin.site.register(Client)
admin.site.register(Place)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Ticket)
