from django.contrib import admin

from main.models import Student

# Register your models here.
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
admin.site.register(Student, StudentsAdmin)