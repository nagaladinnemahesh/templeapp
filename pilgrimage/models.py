from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

from django.db import models
from django.contrib.auth.models import User

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

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="Your Name")  # Add this line
    email = models.EmailField(default="Your Email")
    date_of_visit = models.DateField(default=timezone.now)
    service = models.CharField(max_length=15, choices=Pilgrim.SERVICE_CHOICES, default='Suprabatha')

    def __str__(self):
        return f'{self.user.username} - {self.name} - {self.service}'
