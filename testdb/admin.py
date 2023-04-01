from django.contrib import admin

from testdb.models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass
