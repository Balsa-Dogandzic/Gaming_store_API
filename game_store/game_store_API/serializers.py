"""Define your serializers here"""
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework import  serializers
from game_store.settings import SIMPLE_JWT
from .models import (Component,ComponentType,Manufacturer,Product,
ProductCategory,Specifications,User,Rating)
# pylint: disable=too-few-public-methods


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for user registration"""
    class Meta:
        """Meta class for this serializer"""
        model = User
        fields = ('id','username','email','password','first_name', 'last_name')
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'],
            password = validated_data['password'],email = validated_data['email'],
            first_name=validated_data['first_name'],last_name=validated_data['last_name'])
        return user


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Hyperlinked user serializer"""
    class Meta:
        """Meta class for this serializer"""
        model = User
        fields = ['id','url','username','email','password','first_name',
        'last_name','is_active','admin','date_joined','last_login']


class LoginSerializer(serializers.ModelSerializer):
    """User serializer for login response"""
    class Meta:
        """Meta class for this serializer"""
        model = User
        fields = ['id','username','email','password','first_name','last_name',
        'is_active','admin','date_joined','last_login']


class TokenObtainPairSerializer(TokenObtainSerializer):
    """Overwritten jwt login serializer"""
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

    def create(self, validated_data):
        return

    def update(self, instance, validated_data):
        return

class CategorySerializer(serializers.ModelSerializer):
    """Category serializer"""
    class Meta:
        """Meta class for this serializer"""
        model = ProductCategory
        fields = '__all__'


class ManufacturerSerializer(serializers.ModelSerializer):
    """Manufacturer serializer"""
    class Meta:
        """Meta class for this serializer"""
        model = Manufacturer
        fields = '__all__'


class ComponentTypeSerializer(serializers.ModelSerializer):
    """Component type serializer"""
    class Meta:
        """Meta class for this serializer"""
        model = ComponentType
        fields = '__all__'


class ComponentSerializer(serializers.ModelSerializer):
    """Component serializer"""
    class Meta:
        """Meta class for this serializer"""
        model = Component
        fields = "__all__"

class DetailedComponentSerializers(serializers.ModelSerializer):
    """Component serializer with more data"""
    type = serializers.SlugRelatedField(read_only=True, slug_field='name')
    manufacturer = serializers.SlugRelatedField(read_only=True, slug_field='name')
    class Meta:
        """Meta class for this serializer"""
        model = Component
        fields = ['id','name','type','manufacturer']


class ProductSerializer(serializers.ModelSerializer):
    """Product serializer"""
    class Meta:
        """Meta class for this serializer"""
        model = Product
        fields = '__all__'


class ProductListSerializer(serializers.HyperlinkedModelSerializer):
    """Product serializer for list method in views"""
    category = serializers.SlugRelatedField(read_only=True, slug_field='name')
    manufacturer = serializers.SlugRelatedField(read_only=True, slug_field='name')
    class Meta:
        """Meta class for this serializer"""
        model = Product
        fields = ['id','name','url','category','manufacturer','image',
            'description','price','average_rating']


class SpecificationSerializer(serializers.ModelSerializer):
    """Specs serializer"""
    class Meta:
        """Meta class for this serializer"""
        model = Specifications
        fields = '__all__'


class SpecificationDetailSerializer(serializers.ModelSerializer):
    """Specs serializer to display components"""
    component = DetailedComponentSerializers(read_only=True)
    class Meta:
        """Meta class for this serializer"""
        model = Specifications
        fields = ['id','component','quantity']

class ProductRetrieveSerializer(serializers.HyperlinkedModelSerializer):
    """Product serializer for retrieve method in views"""
    category = serializers.SlugRelatedField(read_only=True, slug_field='name')
    manufacturer = serializers.SlugRelatedField(read_only=True, slug_field='name')
    specs = SpecificationDetailSerializer(read_only=True, many=True)
    class Meta:
        """Meta class for this serializer"""
        model = Product
        fields = ['id','name','url','category','manufacturer','image','description',
            'price','average_rating','specs']

class RatingSerializer(serializers.ModelSerializer):
    """Rating serializer"""
    class Meta:
        """Meta class for ratings"""
    model = Rating
    fields = '__all__'
