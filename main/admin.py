from django.contrib import admin
from .models import Config, Contact, Portfolio, Team, SocialNetworks, TeamNetwork, Partners

# Register your models here.

admin.site.register(Config)
admin.site.register(Contact)
admin.site.register(Portfolio)
admin.site.register(Team)
admin.site.register(SocialNetworks)
admin.site.register(TeamNetwork)
admin.site.register(Partners)