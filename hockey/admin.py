from django.contrib import admin

# Register your models here.
from hockey.models import HockeyEvent

admin.site.register(HockeyEvent)
