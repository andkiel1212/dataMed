from django.db import models
from patients.models import Patient
import uuid

class Visit(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="visit")
    

