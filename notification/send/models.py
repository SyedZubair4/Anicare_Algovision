from django.db import models
from django.conf import settings
import os
from django.core.validators import EmailValidator

# from django.contrib.gis.db import models

class UserSubmission(models.Model):
    user_name = models.CharField(max_length=100)
    submission_data = models.TextField()
    submission_time = models.DateTimeField(auto_now_add=True)


class ngoForm(models.Model):
    ngoUserName = models.CharField(max_length=20)
    ngoPhoneNumber = models.IntegerField()
    ngoImage = models.ImageField()
    # ngoLocation = models.PointField()
    ngoDesc = models.TextField()
    ngoAniType = models.CharField(max_length=10)
    ngoAniPriority = models.CharField(max_length=15)


class AnimalReport(models.Model):
    user_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='animal_photos/')
    location = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()
    ANIMAL_TYPE_CHOICES = [('Pet', 'Pet'), ('Stray', 'Stray')]
    animal_type = models.CharField(max_length=5, choices=ANIMAL_TYPE_CHOICES)
    PRIORITY_CHOICES = [('Emergency', 'Emergency'), ('Urgent', 'Urgent'), ('Not-Urgent', 'Not-Urgent')]
    priority_type = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name


class UploadFile(models.Model):
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.file.name
    
    def save(self, *args, **kwargs):
        # Get the base directory of the Django project
        base_directory = settings.BASE_DIR
        # Define the full path where the file will be saved
        file_path = os.path.join(base_directory, 'uploads', self.file.name)
        super().save(*args, **kwargs)
