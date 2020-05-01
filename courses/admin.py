from django.contrib import admin

from courses.models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'educator','picture')
    search_fields = ('name',)


admin.site.register(Course, CourseAdmin)
