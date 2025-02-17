from .serializers import PatientSerializer
from .models import Patient

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

# GET /api/patients => Listar
# POST /api/patients => Crear
class ListPatientsView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

# GET /api/patients/<pk> => Detalle
# PUT /api/patients/<pk> => Modificacion
# DELETE /api/patients/<pk> => Borrar
class DetailPatientView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()



        
