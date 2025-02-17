from rest_framework import viewsets
from .models import Appointment, MedicalNote
from .serializers import AppointmentSerializer, MedicalNoteSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    """ViewSet para manejar citas médicas (CRUD completo)"""
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

class MedicalNoteViewSet(viewsets.ModelViewSet):
    """ViewSet para manejar notas médicas (CRUD completo)"""
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()
