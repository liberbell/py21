from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=40, verbose_name="first name")
    last_name = models.CharField(max_length=40)

    def _get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    full_name = property(_get_full_name)
    
    def __str__(self):
        return "{0}".format(self.full_name)
