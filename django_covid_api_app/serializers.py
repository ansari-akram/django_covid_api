from rest_framework import serializers
from .models import User_tbl, FileUpload, Appointment, AppointmentType, Test, TestType, AdminUser


class User_tblSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User_tbl
        fields = ('email_id', 'username', 'password', 'firstname', 'lastname', 'mobile_no')


class User_tblSerializer2(serializers.ModelSerializer):
    class Meta:
        model = User_tbl
        fields = ('email_id', 'username', 'password', 'firstname', 'lastname', 'mobile_no')


class FileSerrializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = ['username', 'file_upload']


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['username', 'appointment_type', 'appointment_date_time', 'created_date', 'created_by']


class AppointmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentType
        fields = ['appointment_type']


class TestTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestType
        fields = ['test_name']


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['username', 'test_type', 'file_upload', 'test_date', 'created_date', 'created_by', 'is_active']


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUser
        fields = ['admin_user', 'admin_pass']