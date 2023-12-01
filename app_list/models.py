from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=20, )
    address = models.TextField()
    roll_numbers = models.IntegerField(unique=True)

    def __str__(self) -> str:
        return self.name