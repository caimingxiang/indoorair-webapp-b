from rest_framework import serializers
from foundation.models import ArchivedWebPage
from rest_framework.validators import UniqueTogetherValidator


class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(required = False)
    last_name = serializers.CharField(required = False)
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())
    )
    password = serializers.CharField()



    def create(self, validated_data):
        first_name = validated_data.get('first_name', None)
        last_name = validated_data.get('last_name', None)
        email = validated_data.get('email', None)
        username = validated_data.get('username', None)
        password = validated_data.get('password', None)

        user = User.objects.create_user(username, email, password)
        user.last_name = last_name
        user.first_name = first_name
        user.save()
        return user
