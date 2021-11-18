from rest_framework import serializers
from adoptLifeApp.models.pqrs import Pqrs

class PqrsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pqrs
        fields = ['pqrs_id', 'user_id', 'title', 'comment', 'date']