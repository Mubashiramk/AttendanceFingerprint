from django.db import models


class studenttable(models.Model):
    sid = models.CharField(max_length=20, null=False, unique=True,
                                verbose_name="Student ID",
                                help_text="Student ID")
    name = models.CharField(max_length=20, null=False, unique=False,
                                verbose_name="Student Name",
                                help_text="Student Name")
    status = models.CharField(max_length=10, null=True, unique=False,
                                verbose_name="Status", default="-",
                                help_text="Status: P/A")

    def __str__(self):
        return self.sid.join(self.name.join(self.status))
