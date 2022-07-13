from rest_framework import  serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','password','first_name', 'last_name')
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'],password = validated_data['password'],email = validated_data['email'],
            first_name=validated_data['first_name'],last_name=validated_data['last_name'])
        return user

# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass