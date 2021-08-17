from django.db import models

from datetime import time

from django.db.models.deletion import CASCADE

class Room(models.Model):
    name = models.CharField(max_length=50)
    floor_number = models.IntegerField(default=None)
    room_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}: room {self.room_number} on floor {self.floor_number}"

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"

    # def hello(self, s):
    #     print("Hello from meeting!" + s)





# Create your models here.
