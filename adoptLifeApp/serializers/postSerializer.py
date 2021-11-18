from rest_framework import serializers
from adoptLifeApp.models.post import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['post_id', 'user_id', 'pet_gender', 'pet_name', 'pet_age', 'pet_city', 'photo']
