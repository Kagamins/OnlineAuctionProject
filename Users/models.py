from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    Phone_num = models.IntegerField(null=True,blank=True)
    twitter_id = models.CharField(max_length=50, null=True, blank=True, default="")
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)



    def __unicode__(self):
        return u"{} : {}".format(self.name, self.pk)

    def __str__(self):
        return "{} : {}".format(self.name, self.pk)
    def signup(self, request, user):
        User.objects.create(
            user=user,
            name=user.username,
            email=user.email,
            twitter_id=self.cleaned_data.get('twitter_id')
        )
