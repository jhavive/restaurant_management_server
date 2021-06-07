from django.contrib import admin
from .models import User

print(User)
admin.site.register(User)