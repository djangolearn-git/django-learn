from django.db import models

class Appsettings(models.Model):
    key = models.CharField(max_length=32, primary_key=True)
    value = models.CharField(max_length=128,blank=True, default='')

    def __str__(self):
        return self.key
