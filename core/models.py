# core/models.py
from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    bio = models.TextField()
    
    # New image field
    photo = models.ImageField(upload_to='candidate_photos/', blank=True, null=True)

    def __str__(self):
        return self.name


class Testimony(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    # Add image field
    photo = models.ImageField(upload_to='testimony_photos/', null=True, blank=True)

    def __str__(self):
        return self.name
