from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Appointment, MedicalNote
from .serializers import AppointmentSerializer, MedicalNoteSerializer

# GET /api/appointments => Listar
# POST /api/appointments => Crear
class ListAppointmentsView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

# GET /api/appointments/<pk> => Detalle
# PUT /api/appointments/<pk> => Modificación
# DELETE /api/appointments/<pk> => Borrar
class DetailAppointmentView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

# GET /api/medical-notes => Listar
# POST /api/medical-notes => Crear
class ListMedicalNotesView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()

# GET /api/medical-notes/<pk> => Detalle
# PUT /api/medical-notes/<pk> => Modificación
# DELETE /api/medical-notes/<pk> => Borrar
class DetailMedicalNoteView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()

