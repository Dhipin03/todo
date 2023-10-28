from django.db import models

class task(models.Model):
    STATUS_CHOICES = (
        ('completed', 'Completed'),
        ('pending', 'Pending'),
        ('expired', 'Expired'),
    )

    name = models.CharField(max_length=250)
    priority = models.IntegerField()
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.name
