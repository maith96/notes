from django.db import models

# Create your models here.
from django.contrib.auth.models import User, UserManager
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

import uuid
import os

from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

def get_avatar_path(instance, filename):
    ext = filename.split('.')[-1]  # Get the file extension
    filename = f"{uuid.uuid4()}.{ext}"  # Create a new filename with a UUID
    return os.path.join('avatars', filename)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username,avatar, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email = self.normalize_email(email), 
            username = username, avatar=avatar)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    def create_superuser(self, email,avatar,username, password):
        user = self.model(
            email = self.normalize_email(email), 
            username = username,
            password=password, avatar=avatar
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    avatar = models.ImageField(upload_to=get_avatar_path, null=True, blank=True, default='')
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'password', 'username']
    
    def save(self, *args, **kwargs):
        # If avatar is uploaded
        if self.avatar:
            img = Image.open(self.avatar)
            img_io = BytesIO()
            img.save(img_io, format='WEBP')  # Save as WebP with quality setting
            img_content = ContentFile(img_io.getvalue(), name=f"{uuid.uuid4()}.webp")
            self.avatar = img_content

        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

class Note(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
