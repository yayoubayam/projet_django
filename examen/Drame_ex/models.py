from django.db import models

from django.db import models
class User(models.Model):
    username = models.CharField(max_length = 200)
    # Email = models.TextField(max_length = 200)
    password = models.CharField(max_length = 200)

    def __str__(self):
        return self.username
class Tâche(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True,blank=True)
    completed = models.BooleanField(default=False)
    date_update = models.DateTimeField(auto_now=True)
    date_creation = models.DateField(auto_now_add=True)
    userpk = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
    	return self.title
       

# Create your models here.
