from django.db import models

#Create your models here.
class Affiliations(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=50)
class Occupations(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=50)
class Character(models.Model):
    def __str__(self):
        return self.name
    def returnAll(self):
        return [self.name,affiliations.name,occupations.name]
    name=models.CharField(max_length=50)
    manage_debut=models.IntegerField()
    anime_debut=models.IntegerField()
    affiliations=models.ManyToManyField(Affiliations)
    occupations=models.ManyToManyField(Occupations)
