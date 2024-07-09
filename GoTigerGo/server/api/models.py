from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Shirt(models.Model):
    team = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    number = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    size = models.PositiveIntegerField(validators=[
        MinValueValidator(30),
        MaxValueValidator(60),
    ])
    is_guest = models.BooleanField()

    def __str__(self):
        return f"{self.surname} {self.number} ({self.team})"
