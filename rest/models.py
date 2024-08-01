from django.db import models

# Create your models here.

class Bank(models.Model):
    name=models.CharField(max_length=100)
    father_name=models.CharField(max_length=40)
    Ac=models.IntegerField()
    
    def __str__(self):
        return self.name