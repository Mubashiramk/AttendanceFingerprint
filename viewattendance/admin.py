from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
from viewattendance.models import Student, Branch, Classroom, Teacher, Course


class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'student_name', 'class_id', 'profile_image')


class BranchAdmin(admin.ModelAdmin):
    list_display = ('branch_name',)


class ClassAdmin(admin.ModelAdmin):
    list_display = ('class_id', 'branch_name')


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_id', 'teacher_name', 'branch_name', 'profile_image')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'course_name', 'branch_name')


admin.site.register(Student, StudentAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Classroom, ClassAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Course, CourseAdmin)