from django.db import models
import datetime


class AdminUser(models.Model):
    admin_user = models.CharField(max_length=30)
    admin_pass = models.CharField(max_length=30)

    def __str__(self):
        return self.admin_user


class User_tbl(models.Model):
    username = models.CharField('USERNAME', max_length=30, primary_key=True)
    email_id = models.EmailField('EMAIL ID', max_length=60)
    password = models.CharField('PASSWORD', max_length=30)
    firstname = models.CharField('FIRST NAME', max_length=30)
    lastname = models.CharField('LAST NAME', max_length=30)
    mobile_no = models.IntegerField('MOBILE NO.:')

    def __str__(self):
        return self.username


class FileUpload(models.Model):
    username = models.ForeignKey(User_tbl, on_delete=models.CASCADE)
    file_upload = models.FileField()
    file_upload_time = models.DateTimeField(default=datetime.datetime.now)


    def __str__(self):
        return self.file_upload.name


class TestType(models.Model):
    test_name = models.CharField(max_length=30)

    def __str__(self):
        return self.test_name


class Test(models.Model):
    username = models.ForeignKey(User_tbl, on_delete=models.CASCADE)
    test_type = models.ForeignKey(TestType, on_delete=models.CASCADE)
    file_upload = models.FileField()
    test_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(AdminUser, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.username.username + " - " + self.test_type.test_name


class AppointmentType(models.Model):
    appointment_type = models.CharField(max_length=30)

    def __str__(self):
        return self.appointment_type


class Appointment(models.Model):
    username = models.ForeignKey(User_tbl, on_delete=models.CASCADE)
    appointment_type = models.ForeignKey(AppointmentType, on_delete=models.CASCADE)
    appointment_date_time = models.DateTimeField()
    created_date = models.DateTimeField()
    created_by = models.ForeignKey(AdminUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.username.username + " - " + self.appointment_type.appointment_type