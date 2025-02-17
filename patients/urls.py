from django.urls import path
from rest_framework.routers import DefaultRouter
from .viewsets import PatientViewSet

router = DefaultRouter()
router.register('patients', PatientViewSet)  

urlpatterns = [] + router.urls  
