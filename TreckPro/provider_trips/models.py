import uuid
from django.db import models
#from django.contrib.auth.models import User

# Create your models here.
class TripModel(models.Model):
    trip_id = models.UUIDField(default=uuid.uuid4, editable=False)
    trip_name = models.CharField(max_length=30)
    created_on = models.DateTimeField (auto_now_add=True)
    starting_destination = models.CharField(max_length=30)
    ending_destination = models.CharField(max_length=30)
    pickup_point = models.CharField(max_length=30)
    droping_point = models.CharField(max_length=30)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    days = models.IntegerField()
    budget = models.FloatField()
    no_of_seats = models.IntegerField()
    booked_seats = models.IntegerField()
    pending_seats = models.IntegerField()
    description = models.CharField(max_length=30)
#    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    is_active = models.BooleanField()
    def __str__(self):
        trip=self.trip_id+'_'+self.trip_name
        return trip


