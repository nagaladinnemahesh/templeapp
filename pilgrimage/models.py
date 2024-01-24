from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Add other fields related to the booking

    def __str__(self):
        return f'{self.user.username} - {self.some_field}' 
    
class Pilgrim(models.Model):
    SERVICE_CHOICES = [
        ('Suprabatha', 'Suprabatha'),
        ('Angapradakshina', 'Angapradakshina'),
        ('Thomala', 'Thomala'),
        ('Kalyanam', 'Kalyanam'),
        ('Bramhotsavam', 'Bramhotsavam'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    date_of_visit = models.DateField()
    service = models.CharField(max_length=15, choices=SERVICE_CHOICES, default='Suprabatha')

    def __str__(self):
        return f'{self.name} - {self.service}'
