from rest_framework import serializers
from adoptLifeApp.models.adoption import Adoption

class AdoptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adoption
        fields = ['adoption_id', 'date', 'user_id', 'post_id']