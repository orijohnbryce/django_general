from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(null=False, max_length=50)
    age = models.IntegerField(null=False)

    class Meta:
        db_table = "person"

    def __str__(self):
        return f"<Person: {self.first_name}"

class Car(models.Model):
    car_type = models.CharField(null=False, max_length=50)
    owner = models.ForeignKey(Person, models.RESTRICT)

    class Meta:
        db_table = "car"


    def __str__(self):
        return f"<Car: {self.car_type}"