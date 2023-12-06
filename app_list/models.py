from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=20 )
    address = models.TextField()
    roll_numbers = models.IntegerField(unique=True)

    def __str__(self) -> str:
        return self.name
    
class subject(models.Model):
    Hindi = "HI"
    English = "EN"
    Math = "MT"
    Science = "SC"
    Geography = "GO"
    SUBJECT_CHOICES = [
        (Hindi, "Hindi"),
        (English, "English"),
        (Math, "Math"),
        (Science, "Science"),
        (Geography, "Geography"),
    ]
    subject_in_school = models.CharField(
        max_length=2,
        choices=SUBJECT_CHOICES,
        default=Hindi,
    )

    student = models.ForeignKey(student, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.student.name

  
    