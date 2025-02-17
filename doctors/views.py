from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Doctor, Department, DoctorAvailability, MedicalNote
from .serializers import (
    DoctorSerializer, 
    DepartmentSerializer, 
    DoctorAvailabilitySerializer, 
    MedicalNoteSerializer
)

# GET /api/doctors => Listar
# POST /api/doctors => Crear
class ListDoctorsView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

# GET /api/doctors/<id> => Detalle
# PUT /api/doctors/<id> => Modificación
# DELETE /api/doctors/<id> => Borrar
class DetailDoctorView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    lookup_field = 'id'

# GET /api/departments => Listar departamentos
# POST /api/departments => Crear departamento
class ListDepartmentsView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

# GET /api/departments/<id> => Detalle
# PUT /api/departments/<id> => Modificación
# DELETE /api/departments/<id> => Borrar
class DetailDepartmentView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    lookup_field = 'id'

# GET /api/doctoravailabilities => Listar disponibilidades
# POST /api/doctoravailabilities => Crear disponibilidad
class ListDoctorAvailabilitiesView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()

# GET /api/doctoravailabilities/<id> => Detalle
# PUT /api/doctoravailabilities/<id> => Modificación
# DELETE /api/doctoravailabilities/<id> => Borrar
class DetailDoctorAvailabilityView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()
    lookup_field = 'id'

# GET /api/medicalnotes => Listar notas médicas
# POST /api/medicalnotes => Crear nota médica
class ListMedicalNotesView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()

# GET /api/medicalnotes/<id> => Detalle
# PUT /api/medicalnotes/<id> => Modificación
# DELETE /api/medicalnotes/<id> => Borrar
class DetailMedicalNoteView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()
    lookup_field = 'id'
