from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractUser
)
from django.core.validators import MaxValueValidator, MinValueValidator

class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an email address')
        user = self.model(
            username=self.username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, password):
        user = self.create_user(
            username,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
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
    balance = models.DecimalField(max_digits=6, decimal_places=2, default=1000,validators=[MaxValueValidator(1000),MinValueValidator(0)])
    objects: MyUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


class ProductCategory(models.Model):
    name = models.CharField(max_length=32,unique=True)
    image = models.FileField(upload_to='categories/')

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=32,unique=True)

    def __str__(self):
        return self.name

    
class ComponentType(models.Model):
    name = models.CharField(max_length=32,unique=True)

    def __str__(self):
        return self.name


class Component(models.Model):
    name = models.CharField(max_length=32)
    type = models.ForeignKey(ComponentType,on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=32)
    image = models.FileField(upload_to='products/')
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2,validators=[MaxValueValidator(1000),MinValueValidator(0)])
    category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Specifications(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    component = models.ForeignKey(Component,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1,validators=[MaxValueValidator(10),MinValueValidator(1)])