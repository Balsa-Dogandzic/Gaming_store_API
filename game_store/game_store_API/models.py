"""Make your models here"""
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractUser
)
from django.core.validators import MaxValueValidator, MinValueValidator
# pylint: disable=too-few-public-methods
# pylint: disable=no-member

class MyUserManager(BaseUserManager):
    """Manager for the User model"""
    def create_user(self, username, password=None):
        """Create a default user"""
        if not username:
            raise ValueError('Users must have an email address')
        user = self.model(
            username=self.username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, password):
        """Create a staff user"""
        user = self.create_user(
            username,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """Create a superuser user"""
        user = self.create_user(
            username,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    """Custom user module"""
    username = models.CharField(max_length=32, unique=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    is_active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    balance = models.FloatField(default=1000,
        validators=[MaxValueValidator(1000),MinValueValidator(0)])
    avatar = models.FileField(upload_to='avatars/',null=True)
    objects: MyUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


class ProductCategory(models.Model):
    """Category model"""
    name = models.CharField(max_length=32,unique=True)
    image = models.FileField(upload_to='categories/')

    def __str__(self):
        return str(self.name)


class Manufacturer(models.Model):
    """Manufacturer model"""
    name = models.CharField(max_length=32,unique=True)

    def __str__(self):
        return str(self.name)


class ComponentType(models.Model):
    """Component type model"""
    name = models.CharField(max_length=32,unique=True)

    def __str__(self):
        return str(self.name)


class Component(models.Model):
    """Component model"""
    name = models.CharField(max_length=32)
    type = models.ForeignKey(ComponentType,on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    """Product model"""
    name = models.CharField(max_length=32)
    image = models.FileField(upload_to='products/')
    description = models.TextField()
    price = models.FloatField(validators=[MaxValueValidator(1000),MinValueValidator(0)])
    category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    def average_rating(self):
        """Returns average rating of the product"""
        reviews = Rating.objects.filter(product=self).aggregate(average=models.Avg('rating'))
        average_rating = 0
        if reviews['average'] is not None:
            average_rating = float(reviews['average'])
        return average_rating


class Specifications(models.Model):
    """Specifications model"""
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='specs')
    component = models.ForeignKey(Component,on_delete=models.CASCADE)
    class Meta:
        """Unique together validator"""
        unique_together = ('product','component')

class Rating(models.Model):
    """Rating model"""
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='ratings')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='ratings')
    rating = models.SmallIntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])
    comment = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        """Unique together validator"""
        unique_together = ('user','product')

class Order(models.Model):
    """Order class"""
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='orders')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='order')
    quantity = models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(1)])

    def total(self):
        """Returns the total cost of the order"""
        return self.product.price * self.quantity
