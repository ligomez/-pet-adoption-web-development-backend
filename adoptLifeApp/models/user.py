from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, identity_document, name, email, city, password):
        if not identity_document or not email:
            raise ValueError('Identity Document and Email is required')
        
        user = self.model(
            identity_document=identity_document, 
            name=name, 
            email=self.normalize_email(email), 
            city=city,
            username=username
        ) 

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, identity_document, name, email, city, password):
        user = self.create_user(
            identity_document=identity_document, 
            name=name, 
            email=self.normalize_email(email), 
            city=city,
            username=username,
            password=password
        )

        user.admin = True
        user.save()
        return user

class User(AbstractBaseUser):
    user_id = models.BigAutoField(primary_key=True)
    identity_document = models.IntegerField('Identity Document', unique=True, null=False)
    name = models.CharField('Name', max_length=50, null=False)
    email = models.EmailField('Email', max_length=80, unique=True, null=False)
    city = models.CharField('City', max_length=50)
    address = models.CharField('Address', max_length=100, null=True)
    username = models.CharField('Username', max_length=30, unique=True, null=False)
    phone_number = models.CharField('Phone Number', max_length=15, null=True)
    admin = models.BooleanField(default=False)
    image = models.ImageField(upload_to='users', null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['identity_document', 'name', 'email', 'city']

    def __str__(self):
        return f'{self.name} ({self.email})'

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.admin