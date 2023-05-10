from django.db import models

#Create your models here.
class Character(models.Model):
    def __str__(self):
        return self.name
    def returnAll(self):
        return [self.name,affiliations.name,occupations.name]
    
    name=models.CharField(max_length=50)
    anime_debut=models.IntegerField()
    affiliations=models.CharField( max_length=150)
    occupations=models.CharField( max_length=150)
    birthday=models.CharField(max_length=50)
    url=models.CharField(max_length=300)
