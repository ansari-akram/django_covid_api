import os
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User_tbl, FileUpload, Test, TestType, AppointmentType, Appointment, AdminUser
from .serializers import User_tblSerializer, FileSerrializer, TestSerializer, TestTypeSerializer, AppointmentSerializer, AppointmentTypeSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser, FileUploadParser
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from.serializers import AdminSerializer


class Appointment_typeViewSet(viewsets.ModelViewSet):
    queryset = AppointmentType.objects.all()
    serializer_class = AppointmentTypeSerializer


class Admin_userViewSet(viewsets.ModelViewSet):
    queryset = AdminUser.objects.all().order_by('admin_user')
    serializer_class = AdminSerializer


class User_tblViewSet(viewsets.ModelViewSet):
    queryset = User_tbl.objects.all().order_by('username')
    serializer_class = User_tblSerializer


@api_view(['GET', 'POST', 'DELETE'])
def get_list(request):
    if request.method == 'GET':
        users = User_tbl.objects.all()
        user_serializer = User_tblSerializer(users, many=True)
        return JsonResponse(user_serializer.data, safe=False)
    
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = User_tblSerializer(data=user_data)

        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def get_detail_list(request, username):
    try:
        users = User_tbl.objects.get(username=username)
    except User_tbl.DoesNotExist:
        return JsonResponse({'message': 'user does not exists.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        user_serializer = User_tblSerializer(users)
        return JsonResponse(user_serializer.data)
    
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user_serializer = User_tblSerializer(users, data=user_data)

        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        users.delete()
        return JsonResponse({'message': 'User deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)

# username=cmd&email_id=cmd@cmd.com&password=cmd&firstname=cmd&lastname=cmd&mobile_no=1234567890

class FileUploadViewSet(viewsets.ModelViewSet):
    queryset = FileUpload.objects.all()
    serializer_class = FileSerrializer
    
    def create(self, request):
        file_upload = request.FILES.get('file_upload')
        user = request.POST.get("username")
        content_type = file_upload.content_type
        file_path = user + "/" + file_upload.name
        _path = default_storage.save(user + "/" + file_upload.name, ContentFile(file_upload.read()))
        response = "POST API uploaded file " + content_type + " file."
        user_ins = User_tbl.objects.get(username=user)
        FileUpload.objects.create(username=user_ins, file_upload=file_path)
        print("================================================================")
        return Response(response)
    
    def post(self, request, *args, **kwargs):
        pdf_serializer = FileSerrializer(data=request.data)
        if pdf_serializer.is_valid():
            pdf_serializer.save()
            return Response(pdf_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(pdf_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    def create(self, request):
        file_upload = request.FILES.get('file_upload')
        user = request.POST.get('username')
        content_type = file_upload.content_type
        test_no = int(request.POST.get('test_type'))
        test = TestType.objects.all()[test_no - 1]
        test = test.test_name
        file_path = user + "/" + test + "/" + file_upload.name
        _path = default_storage.save(file_path, ContentFile(file_upload.read()))
        response = "POST API uploaded test."

        admin_user_no = int(request.POST.get('created_by'))

        # creating entry to database table
        user_ins = User_tbl.objects.get(username=user)
        test_type_ins = TestType.objects.get(test_name=test)
        test_date_ins = request.POST.get('test_date')
        admin_user = AdminUser.objects.all()[admin_user_no - 1]
        is_active_ins = request.POST.get('is_active')
        is_active_ins = True if is_active_ins == "true" else False
        # print('[info]', Test.objects.all())
        # print('info', user_ins, test_type_ins, file_path, test_date_ins, admin_user, is_active_ins)
        Test.objects.create(username=user_ins, test_type=test_type_ins, file_upload=file_path, test_date=test_date_ins, created_by=admin_user, is_active=is_active_ins)
        # Test.objects.create(username=user, test_type=test, file_upload=file_path, )
        return Response(response)

    def post(self, request, *args, **kwargs):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestTypeViewSet(viewsets.ModelViewSet):
    queryset = TestType.objects.all()
    serializer_class = TestTypeSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class AppointmentTypeViewSet(viewsets.ModelViewSet):
    queryset = AppointmentType.objects.all()
    serializer_class = AppointmentTypeSerializer