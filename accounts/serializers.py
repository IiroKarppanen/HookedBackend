from rest_framework import serializers
from . models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'password', 'watchlist']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        print("PASSWORD")
        print(password)
        instance = self.Meta.model(**validated_data)
        print(instance)
        if password is not None:
            instance.set_password(password)
        print("TOIMII VIELÄ")
        instance.save()
        return instance