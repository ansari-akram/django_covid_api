from django.contrib import admin
from .models import User_tbl, FileUpload, Appointment, AppointmentType, Test, TestType, AdminUser


admin.site.register(User_tbl)
admin.site.register(FileUpload)
admin.site.register(AppointmentType)
admin.site.register(Appointment)
admin.site.register(Test)
admin.site.register(TestType)
admin.site.register(AdminUser)