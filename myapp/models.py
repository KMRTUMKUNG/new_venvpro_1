from django.db import models

# Create your models here.
class person(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.IntegerField()
    mail = models.CharField(max_length=50)
    Phone = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Name : " + self.name +" Age : " +str(self.age) 