from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from patients.models import Patient
from doctors.models import Doctor

class DoctorViewSetTests(TestCase):

    def setUp(self):
        self.patient = Patient.objects.create(
            first_name='John',
            last_name='Doe',
            date_of_birth='1980-01-01',
            contact_number='1234567890',
            email='john.doe@example.com',
            address='123 Elm Street',
            medical_history='None',
        )
        self.doctor = Doctor.objects.create(
            first_name='Jane',
            last_name='Smith',
            qualification='MD',
            contact_number='0987654321',
            email='jane.smith@example.com',
            address='456 Oak Street',
            biography='Dr. Jane Smith is a specialist in internal medicine.',
            is_on_vacation=False,
        )
        self.client = APIClient()

    def test_list_should_return_200(self):
        url = reverse('doctor-appointments', kwargs={'pk': self.doctor.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)