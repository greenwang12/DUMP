from django.db import models
from accounts.models import CustomUser

CATEGORY_CHOICES = [
    ('books', 'Books'),
    ('kits', 'Electronic Kits'),
    ('stationery', 'Stationery'),
    ('sports', 'Sports Equipment'),
]

class Listing(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='listings/')
    is_available = models.BooleanField(default=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
