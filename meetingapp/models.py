from django.db import models
import datetime


class Room(models.Model):
    name = models.CharField(max_length=50)
    floor = models.IntegerField()
    room_number = models.IntegerField()
    def __str__(self):
        return f"{self.name} (pokój {self.room_number}, piętro {self.floor})"

class Meeting(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    start_time = models.TimeField(default = datetime.time(9,0,0))
    duration = models.IntegerField(default = 1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title} o {self.start_time} (czas trwania: {self.duration}h)"

