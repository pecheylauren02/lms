from django.contrib import admin

from django.contrib import admin
from .models import User, Student, Admin, Grade

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Admin)
admin.site.register(Grade)
