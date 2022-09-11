from pyexpat import model
from django.db import models

# Create your models here.
YOUR_INTEREST = (
    ('xray_technician','xray_technician'),
    ('second','second'),
    ('third','third'),
    ('fourth','fourth')
)
class Registration(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    your_interest = models.CharField(choices=YOUR_INTEREST, max_length=20)