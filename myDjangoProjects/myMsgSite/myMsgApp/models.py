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
class Mail(models.Model):
    MAILING_LIST_CHOISE = (
                           ('GO', 'Gina Ortiz'),
                           ('RT', 'Rick Tallon'),
                           ('MF', 'Matt Foster'),
                           )
    mail_to = models.CharField(max_length=2, choices=MAILING_LIST_CHOISE, default='GO', verbose_name='Send mail to')
    subject = models.CharField(max_length=150, blank=False)
    mail_date = models.DateTimeField(auto_now=True)
    message = models.TextField(blank=False)
    