from django.db import models


class studenttable(models.Model):
    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'
    sid = models.CharField(max_length=20, null=False, unique=True,
                           verbose_name="Student ID",
                           help_text="Student ID")
    name = models.CharField(max_length=20, null=False, unique=False,
                            verbose_name="Student Name",
                            help_text="Student Name")
    status = models.CharField(max_length=10, null=True, unique=False,
                              verbose_name="Status", default="A",
                              help_text="Status: P/A")

    def __str__(self):
        return self.sid.join(self.name.join(self.status))


class attendancetable(models.Model):
    class Meta:
        verbose_name = 'attendance'
        verbose_name_plural = 'attendance details'
    sid = models.CharField(max_length=20, null=False, unique=True,
                           verbose_name="Student ID",
                           help_text="Student ID")
    cname = models.CharField(max_length=20, null=False, unique=True,
                             verbose_name="class",
                             help_text="class")
    date = models.CharField(max_length=20, null=False, unique=True,
                            verbose_name="date",
                            help_text="date")
    hour = models.CharField(max_length=20, null=False, unique=True,
                            verbose_name="hour",
                            help_text="hour")
    status = models.CharField(max_length=20, null=False, unique=True,
                              verbose_name="status",
                              help_text="status")

    def __str__(self):
        return self.sid.join(self.sid.join(self.cname.join(self.date.join(self.hour.join(self.status)))))
