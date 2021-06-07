# from django.db import models
# from django.contrib.auth.models import AbstractUser
#
#
# class Organization(models.Model):
#     name = models.CharField(max_length=100)
#     logo = models.CharField(max_length=50)
#
# class User(AbstractUser):
#     # organization = models.CharField(max_length=100, blank=True, null=True)
#
#     organization = models.ForeignKey('Organization', blank=False, null=True, on_delete=models.CASCADE)
#     is_root_login = models.BooleanField(null=True)



