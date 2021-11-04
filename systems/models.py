from django.db import models

class contact (models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    message = models.TextField(max_length=300)

    def __str__(self):
        return self.message
    