from django.db import models
from django.contrib.auth.models import User
import uuid
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save, post_delete
# Create your models here.


class Profile(models.Model):
    # profile has one user
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=140, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=140, blank=True, null=True)
    phone = PhoneNumberField(max_length=12, null=True,
                             blank=True, unique=True)
    head_line = models.CharField(max_length=300, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(
        null=True, blank=True, upload_to="profiles/", default="profiles/user-default.png")
    social_github = models.CharField(max_length=200, blank=False, null=True)
    social_linkedIn = models.CharField(max_length=200, blank=False, null=True)
    social_stackOverflow = models.CharField(
        max_length=200, blank=True, null=False)
    social_website = models.CharField(max_length=200, blank=True, null=False)
    social_twitter = models.CharField(max_length=200, blank=True, null=False)
    created = models.DateTimeField(auto_now_add=True)
    location = models.OneToOneField(
        'Location', blank=True, null=True, on_delete=models.SET_NULL)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.user.username)

    # Notes shift + alt + down or up To duplicate
    # https://pythonrepo.com/repo/caioariede-django-location-field--python-geolocation


class Location(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Skill(models.Model):
    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name
