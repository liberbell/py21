from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=40, verbose_name="first name")
    last_name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name
