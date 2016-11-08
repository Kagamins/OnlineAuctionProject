from django.db import models
import os


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class item(models.Model):
    product_name = models.CharField(max_length=18,help_text=('Car_Name'))
    manufacture_year = models.CharField(
        max_length=120, help_text=('E.g.: 2015/2016'))

    picture = models.FileField()
    product_description = models.TextField()
    def get_absolute_url(self):
        return reverse(
            'Create_Auction',
            kwargs={'user': self.pk})


class auction(models.Model):
    product = models.ForeignKey(item)
    auction_date = models.DateField()
    auction_time = models.TimeField()
