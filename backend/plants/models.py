from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
