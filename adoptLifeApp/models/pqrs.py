from django.db import models
from .user import User

class Pqrs(models.Model):
    pqrs_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, related_name="my_pqrs", on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    date = models.DateTimeField(null=True)
    