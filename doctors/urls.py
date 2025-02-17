from django.urls import path
from .views import (
    ListDoctorsView, DetailDoctorView,
    ListDepartmentsView, DetailDepartmentView,
    ListDoctorAvailabilitiesView, DetailDoctorAvailabilityView,
    ListMedicalNotesView, DetailMedicalNoteView
)
from rest_framework.routers import DefaultRouter
from .viewsets import DoctorViewSet

router = DefaultRouter()
router.register('doctors', DoctorViewSet)

urlpatterns = [
    path('departments/', ListDepartmentsView.as_view(), name='list-departments'),
    path('departments/<int:id>/', DetailDepartmentView.as_view(), name='detail-department'),
    path('doctoravailabilities/', ListDoctorAvailabilitiesView.as_view(), name='list-doctor-availabilities'),
    path('doctoravailabilities/<int:id>/', DetailDoctorAvailabilityView.as_view(), name='detail-doctor-availability'),
    path('medicalnotes/', ListMedicalNotesView.as_view(), name='list-medical-notes'),
    path('medicalnotes/<int:id>/', DetailMedicalNoteView.as_view(), name='detail-medical-note'),
] + router.urls
