from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
from viewattendance.models import Student, Branch, Classroom, Teacher, Course, Teaching, Enrollment, Attendance


class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'student_name', 'class_id', 'roll_no')


class BranchAdmin(admin.ModelAdmin):
    list_display = ('branch_name',)


class ClassAdmin(admin.ModelAdmin):
    list_display = ('class_id', 'branch_name')


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_id', 'teacher_name', 'branch_name')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'course_name', 'branch_name')


class TeachingAdmin(admin.ModelAdmin):
    list_display = ('teacher_id', 'course_id', 'class_id')


class EnrollAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'course_id')


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'course_id','status','hour','class_id','date')


admin.site.register(Student, StudentAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Classroom, ClassAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Teaching, TeachingAdmin)
admin.site.register(Enrollment, EnrollAdmin)
admin.site.register(Attendance, AttendanceAdmin)
