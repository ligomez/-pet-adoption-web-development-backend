from django.db import models
from .user import User
from .post import Post

class Adoption(models.Model):
    adoption_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, related_name="my_adoptions", on_delete=models.SET_NULL, null=True)
    post_id = models.OneToOneField(Post, related_name="adopted", on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField()