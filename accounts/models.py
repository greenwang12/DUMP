from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    college_id = models.CharField(max_length=20, unique=True)
    is_verified = models.BooleanField(default=False)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.username
