from django.db import models
from users.models import User

class Patient((models.Model)):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patient")
    patient_name= models.CharField(max_length=100)
    patient_lastname = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    # comment - unset to testing -

    # phone number to add in to the end
    # phone_regex = RegexValidator(
    #    regex=r"^\?1?\d{9,12}$",
    #    message="Numer telefonu musi mieć format : '*********'.",
    # )
    # phone_number = models.CharField(
    #    validators=[phone_regex], max_length=15, blank=False
    # )  # validators should be a list
    email = models.EmailField(max_length=150, blank=False)
    pesel = models.IntegerField()
    birthday = models.DateField()

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


