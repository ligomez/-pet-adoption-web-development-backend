from django.db import models
from .user import User

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, related_name="my_posts", on_delete=models.SET_NULL, null=True, blank=True)
    pet_type = models.CharField(max_length=10, choices=(
        ('P', 'Perro'),
        ('G', 'Gato'),
        ('C', 'Conejo'),
        ('H', 'Hamster'),
        ('A', 'Ave'),
    ))
    pet_gender = models.CharField(max_length=10, choices=(
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    )) 
    pet_name = models.CharField(max_length=20)
    pet_age = models.PositiveIntegerField()
    pet_breed = models.CharField(max_length=20) 
    pet_city = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='posts', null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True)

