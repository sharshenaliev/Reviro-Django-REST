from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveIntegerField()
    quantity_in_stock = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

        indexes = [models.Index(fields=["id"]),
                   models.Index(fields=["name"]),
                   models.Index(fields=["description"]),
                   ]


class Establishment(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=50)
    opening_hour = models.TimeField()
    closing_hour = models.TimeField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

        indexes = [models.Index(fields=["id"]),
                   models.Index(fields=["name"]),
                   models.Index(fields=["description"]),
                   ]
