from django.contrib import admin

# Register your models here.
from .models import Employee

admin.site.register(Employee)# after defining model here we have to register
