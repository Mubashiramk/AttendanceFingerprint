from django.contrib import admin
from uploadapp.models import studenttable

# Register your models here.


class studenttableAdmin(admin.ModelAdmin):
    list_display = ('sid', 'name', 'status')


admin.site.register(studenttable, studenttableAdmin)

