from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=20)
    department = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Employee(models.Model):
    fullname = models.CharField(max_length=20)
    birth_date = models.DateField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname