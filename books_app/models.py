from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
    title = models.TextField()
    author = models.TextField()
    genre = models.TextField()
    status = models.TextField()  # For example, 'متاح', 'تم استعارته', تم بيعه.
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField()

    def __str__(self):
        return f"{self.title} by {self.author}"