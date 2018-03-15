from django.db import models

# Create your models here.
from django.urls import reverse

class Magazin(models.Model):
    maga_name = models.CharField(max_length=200, help_text=" ")
   maga_address = models.CharField(max_length=200, help_text=" ")
   
    phone_number = models.CharField(max_length=200, help_text=" ")

    class Meta:
        ordering = ["maga_name", "maga_address"]


    def get_absolute_url(self):
        return reverse('magazin-detail', args=[str(self.id)])

    def __str__(self):
        return '{0},{1}'.format(self.maga_name, self.maga_address)


class Client(models.Model):
    name = models.CharField(max_length=200, help_text=" ")
    gul= models.CharField(max_length=200, help_text=" ")


    class Meta:
        ordering = ["name","gul"]

    def get_absolute_url(self):
        return reverse('client-detail', args=[str(self.id)])

    def __str__(self):
        return '{0},{1}'.format(self.name,self.gul)

