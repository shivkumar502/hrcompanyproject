from django.contrib import admin
from app.models import Events
# Register your models here.

class EventsAdmin(admin.ModelAdmin):
    list_display = ('events_name','meeting_date_time','created_at','updated_at')
admin.site.register(Events,EventsAdmin)
