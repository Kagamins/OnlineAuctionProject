from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
# Create your models here.

class ticket(models.Model):
    CHOICES = (('Account support','Account support'),('technical support','technical support'),('transaction support','transaction support'))
    category = models.CharField(max_length=64 ,choices=CHOICES,null=True)
    subject = models.CharField("subject",null=False , max_length = 64 )
    body_of_the_ticket = models.TextField("body of the ticket",max_length=300)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return u'{} : {} : {} '.format(self.user.username, self.category, self.subject)

class FAQ(models.Model):
    CHOICES = (('Account support','Account support'),('technical support','technical support'),('transaction support','transaction support'))
    category = models.CharField("category",max_length=64 ,choices=CHOICES,null=True)
    question = models.CharField("question",max_length=200)
    answer = models.CharField("answer",max_length=300)

    def __str__(self):
        return u' {} : {} '.format( self.category, self.question )
