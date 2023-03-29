from django.db import models
from users.models import User
import re
from django.core.exceptions import ValidationError
from datetime import date


GENDER_CHOICES = (
        ("male", "Mężczyzna"),
        ("female", "Kobieta"),
    )

class Patient((models.Model)):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patient", verbose_name="Dr. prowadzący pacjenta")
    #P1 data
    patient_name = models.CharField(max_length=30)
    patient_lastname = models.CharField(max_length=30)
    pesel = models.IntegerField()  
    birthday = models.DateField(verbose_name="Data urodzenia") # data może automatycznie się generować z PESEL
    gender =  models.CharField( max_length=9, choices=GENDER_CHOICES, default="male", verbose_name="Płeć")
    street = ()
    home_number= ()
    post_code = ()

    phone_number = models.DateField()
    email = models.EmailField(max_length=150, blank=False)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.patient_name, self.patient_lastname)

    def clean(self):
        super().clean()

        #validate pesel
        pattern = re.compile(r'^(\d{11})$')
        if not pattern.match(self.pesel):
            raise ValidationError('Musisz podać 11 cyfrowy numer PESEL. Wprowadzone dane są niepoprawne.')
    
        #validate if patiens has 18 years old error
        today = date.today()
        age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday))
        if age < 18:
            raise ValidationError('Pacjent jest niepełnoletni')