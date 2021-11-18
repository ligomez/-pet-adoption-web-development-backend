from rest_framework import serializers
from adoptLifeApp.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'user_id', 
            'username', 
            'password', 
            'name',
            'identity_document',
            'email',
            'city',
            'address',
            'phone_number',
            'image',
            'admin',
            'last_login'
        ]

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user