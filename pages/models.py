from django.db import models

class Appsettings(models.Model):
    key = models.CharField(max_length=32, primary_key=True)
    value = models.CharField(max_length=128,blank=True, default='')

    def __str__(self):
        return self.key

class Student(models.Model):
    first_name = models.CharField(max_length = 100) 
    last_name = models.CharField(max_length = 100)
    std = models.CharField(max_length = 100)
    batch_number = models.IntegerField()
    dateofbirth = models.DateField()
    division = models.CharField(max_length = 10)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_fullname(self):
        return self.first_name + ' ' + self.last_name
