from django.db import models

# Create your models here.
class TutorialItem(models.Model):
    level=models.IntegerField()
    title=models.TextField()
    distance=models.IntegerField()
    price=models.IntegerField()
    time=models.TextField()
    city=models.TextField()
    gearbox=models.TextField()
 
    

