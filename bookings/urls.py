from django.urls import path
from rest_framework.routers import DefaultRouter
from .viewsets import AppointmentViewSet, MedicalNoteViewSet
from .views import (
    ListAppointmentsView, DetailAppointmentView,
    ListMedicalNotesView, DetailMedicalNoteView
)

router = DefaultRouter()
router.register('appointments', AppointmentViewSet)
router.register('medical-notes', MedicalNoteViewSet)

urlpatterns = [
    path('appointments/', ListAppointmentsView.as_view(), name='list-appointments'),
    path('appointments/<int:pk>/', DetailAppointmentView.as_view(), name='detail-appointment'),
    path('medical-notes/', ListMedicalNotesView.as_view(), name='list-medical-notes'),
    path('medical-notes/<int:pk>/', DetailMedicalNoteView.as_view(), name='detail-medical-note'),
] + router.urls 
