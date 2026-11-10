from django.contrib import admin

from .models import Game, Score, UserProfile

admin.site.register(Game)
admin.site.register(UserProfile)
admin.site.register(Score)
