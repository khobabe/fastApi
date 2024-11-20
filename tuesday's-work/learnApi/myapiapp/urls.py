from django.contrib import admin
from django.urls import path,include
from myapiapp.views import StudentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'studentInformation',StudentViewSet)

urlpatterns = [
    path("",include(router.urls))
]
