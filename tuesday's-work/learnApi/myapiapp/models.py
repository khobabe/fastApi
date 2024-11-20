from django.db import models

# Create your models here.
class StudentInformation(models.Model):
    std_name = models.CharField(max_length=200)
    std_class = models.CharField(max_length=50)
    std_age = models.CharField(max_length=50)
    std_phone = models.IntegerField()
    
    def __self__(self):
        return self.std_name
    