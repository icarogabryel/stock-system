from django.db import models

class Product(models.Model):
    identifier = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    amount = models.IntegerField()

    def __str__(self):
        return self.name
