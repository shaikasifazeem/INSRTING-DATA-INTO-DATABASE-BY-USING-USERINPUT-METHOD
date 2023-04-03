from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_id=models.IntegerField(primary_key=True)

    

class Webpage(models.Model):
    topic_id=models.ForeignKey(Topic,on_delete=models.CASCADE)
    t_name=models.CharField(max_length=100,primary_key=True)
    url=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.t_name


class AccessRecord(models.Model):
    t_name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    date=models.DateField(unique=True)

    def __str__(self):
        return self.author





