from django.db import models

# Create your models here.

class Student(models.Model):
    DIECTIONS = (
        ('Backend', 'Backend'),
        ('Frontend','Frontend'),
        ('UX/UI','UX/Ui'),
        ('Fullstack','Fullstack'),

    )
    GENDERS = (
        ('Male', 'Male'),
        ('Female','Female'),
    )
    full_name = models.CharField(max_length=150)
    age = models.IntegerField()
    direction = models.CharField(max_length=255, choices=DIECTIONS)
    gender = models.CharField(max_length=100, choices=GENDERS)
    