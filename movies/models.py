from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.username 






class Collection(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, blank = True)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=400)
    # movies = models.ManyToManyField(Movie ,  blank=True, related_name="movies")
    
    # def __str__ (self):
    #     return self.title

class Movie (models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    genres = models.CharField(max_length = 100)
    uuid = models.CharField(max_length = 50 , primary_key=True, editable= False, default=1)
    collection = models.ManyToManyField(Collection, related_name="movies" )
    # movies = models.ManyToManyField(Collection ,  blank=True, related_name="movies")
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # def __str__(self):
    #     return self.title

    

    # def __unicode__(self):
    #     return self.id

    # def __str__(self):
    #     return self.id

    



