from rest_framework import  serializers
from game_store.settings import SIMPLE_JWT
from .models import ProductCategory, User
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import update_last_login


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


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','url','username','email','password','first_name','last_name','is_active','admin','date_joined','last_login']


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password','first_name','last_name','is_active','admin','date_joined','last_login']


class TokenObtainPairSerializer(TokenObtainSerializer):
    default_error_messages = {
        "no_active_account": {'message':'No active account with the given credentials'}
    }
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        my_user = User.objects.filter(pk=self.user.id).first()
        if my_user:
            serializer = LoginSerializer(my_user)
            data['user'] = serializer.data

        if SIMPLE_JWT.get('UPDATE_LAST_LOGIN'):
            update_last_login(None, self.user)

        return data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'