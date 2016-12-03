from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    Phone_num = models.IntegerField(null=True,blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)
    address = models.CharField(null=True,blank=True,max_length=64,help_text='Address')
    Date_Of_Birth = models.DateField(null=True,blank=True)
    def get_absolute_url(self):
        return reverse('home', kwargs={'pk': self.pk})


    def __unicode__(self):
        return u"{} : {}".format(self.name, self.pk)

    def __str__(self):
        return "{} : {}".format(self.name, self.pk)

class message(models.Model):
    sender = models.ForeignKey(User, related_name='Sender',)
    receiver = models.ForeignKey(User, related_name='Receiver')
    subject = models.CharField(max_length=64,blank=True,null=True)
    body = models.TextField(max_length=400,null=True)
    date_time_sent = models.DateTimeField(auto_now=True)
    def __str__(self):
        return u"From : {} :To {} : Subject {} ".format(self.sender.name,self.receiver.name,self.subject)
