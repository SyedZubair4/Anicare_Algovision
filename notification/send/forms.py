from django.db import models

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
