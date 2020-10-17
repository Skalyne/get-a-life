from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Npg(models.Model):
    pass

class FullTimeJobs(models.Model):
    pass

class MiddleTimeJobs(models.Model):
    pass

class Houses(models.Model):
    pass

class Vehicles(models.Model):
    pass



class MainCharater(models.Model):

    user_character = models.ForeignKey(User, on_delete = models.CASCADE)

    name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField(default=0)

    health = models.IntegerField(default=100)
    health_per_year = models.IntegerField(default = 0)

    intelligence = models.IntegerField(default=0)
    intelligence_per_year = models.IntegerField(default=10)

    money = models.IntegerField(default=0)
    money_per_year = models.IntegerField(default=0)

    #assets
    buildings = models.ManyToManyField(Houses, related_name="propertis", null=True, blank=True)
    vehicles = models.ManyToManyField(Vehicles, related_name="Vehicles", null=True, blank=True)


    #Occupation
    schedule = models.IntegerField(default=0)

    in_school = models.BooleanField(default=False)
    in_middleschool = models.BooleanField(default=False)
    in_highschool = models.BooleanField(default=False)
    in_university = models.BooleanField(default=False)
    in_higheducation = models.BooleanField(default=False)

    working = models.BooleanField(default=False)
    full_job = models.OneToOneField(FullTimeJobs, related_name="Job", on_delete = models.CASCADE, null=True, blank=True)
    middle_job = models.ManyToManyField(MiddleTimeJobs, null=True, blank=True)



    #Social Things
    friends = models.ManyToManyField (Npg, related_name="Friends", null=True, blank=True)
    partner = models.OneToOneField(Npg, related_name="Partner", on_delete = models.CASCADE, null=True, blank=True)

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')





