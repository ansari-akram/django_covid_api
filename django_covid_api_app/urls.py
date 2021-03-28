from django.urls import include, path
from rest_framework import routers
from . import views
from django.conf.urls import url
from django_covid_api_app import views


router = routers.DefaultRouter()
router.register(r'users_tbl', views.User_tblViewSet, basename='USERS')
router.register(r'upload', views.FileUploadViewSet, basename='upload')
router.register(r'appointment', views.AppointmentViewSet, basename='appointment')
router.register(r'test', views.TestViewSet, basename='test')
router.register(r'admin_tbl', views.Admin_userViewSet, basename='admin_tbl')
router.register(r'test_type', views.TestTypeViewSet, basename='test_type')
router.register(r'appointment_type', views.Appointment_typeViewSet, basename='appointment_type')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('users', views.get_list),
    # path('users/<username>', views.get_detail_list),
]