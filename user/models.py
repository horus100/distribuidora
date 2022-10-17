from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,name,lastname,password=None):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email,name=name,lastname=lastname)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,name,lastname,password):
        user = self.create_user(email,name,lastname,password)
        user.is_superuser = True
        user.is_staff = True
        user.is_worker = True
        user.save(using=self._db)
        return user


class User (AbstractBaseUser,PermissionsMixin):
    """ Usuario personalizado"""
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length= 255)
    lastname = models.CharField(max_length= 255)
    is_active: models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name","lastname"]

    def __str__(self):
        return self.name

class Location(models.Model):
    """ distritos - provincias - departamentos"""
    district = models.CharField(max_length= 50)
    province = models.CharField(max_length= 50)
    department = models.CharField(max_length= 50)

class CustomerCategory(models.Model):
    """ Categorias de la empresa cliente"""
    name = models.CharField(max_length= 50)
    
class Customer(models.Model):
    """ Usuario Empresa cliente """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length= 255)
    ruc = models.CharField(max_length= 11)
    address = models.CharField(max_length= 255)
    reference = models.CharField(max_length= 255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)


