from django.contrib import admin
from .models import Project
from .models import Employee

# Register your models here.
admin.site.register(Project)
admin.site.register(Employee)
