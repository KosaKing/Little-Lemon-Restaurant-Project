from django.db import models

# Create your models here.
class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField()

class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_gues = models.IntegerField()
    BookingDate = models.DateTimeField()