from django.db import models

# Create your models here.
from my_app.models import BaseClass,DistrictChoices

class AcademicCounsellors(BaseClass):

    profile=models.OneToOneField('authentication.Profile',on_delete=models.CASCADE)

    first_name = models.CharField(max_length=25)

    last_name = models.CharField(max_length=25)

    employee_id = models.CharField(max_length=10)

    photo = models.ImageField(upload_to='academic-counsellor')

    email = models.EmailField()

    contact = models.CharField(max_length=12)

    house_name = models.CharField(max_length=25)

    post_office = models.CharField(max_length=25)

    district = models.CharField(max_length=20,choices=DistrictChoices.choices)

    pincode = models.CharField(max_length=6)

    qualification = models.CharField(max_length=10)
    
    stream = models.CharField(max_length=25)

    id_proof = models.FileField(upload_to='academic-counsellor/idproof')

def __str__(self):
        
         return f'{self.first_name} {self.last_name}'
    
class Meta:

        verbose_name = 'academic counsellor'

        verbose_name_plural ='academic counsellor'
