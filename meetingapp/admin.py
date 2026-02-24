from django.contrib import admin

from meetingapp.models import Meeting
from meetingapp.models import Room

admin.site.register(Meeting)
admin.site.register(Room)
