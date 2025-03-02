from django.db import models

import uuid

# Create your models here.

class BaseClass(models.Model):

    uuid= models.SlugField(unique=True,default=uuid.uuid4)

    active_status= models.BooleanField(default=True)

    created_at =models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        abstract = True

class CourseChoices(models.TextChoices):

    # variable = databasevalue + reperesentation


    PY_DJANGO = 'PY-DJANGO','PY DJANGO'

    MEARN = 'MEARN','MEARN'

    DATA_SCIENCE = 'DATA SCIENCE','DATA SCIENCE'

    SOFTWARE_TESTING = 'SOFTWARE TESTING','SOFTWARE TESTING'

class DistrictChoices(models.TextChoices):

    THIRUVANANTHAPURAM = 'THIRUVANANTHAPURAM','THIRUVANANTHAPURAM'

    KOLLAM = 'KOLLAM','KOLLAM'

    PATHANAMTHITTA = 'PATHANAMTHITTA','PATHANAMTHITTA'

    ALAPUZHA = 'ALAPUZHA','ALAPUZHA'

    KOTTAYAM = 'KOTTAYAM','KOTTAYAM'

    IDUKKI = 'IDUKKI','IDUKKI'

    ERNAKULAM = 'ERNAKULAM','ERNAKULAM'

    THRISSUR = 'THRISSUR','THRISSUR'

    PALAKKAD = 'PALAKKAD','PALAKKAD'

    MALAPPURAM = 'MALAPPURAM','MALAPPURAM'

    KOZHIKODE = 'KOZHIKODE','KOZHIKODE'

    WAYANAD = 'WAYANAD','WAYANAD'

    KANNUR = 'KANNUR','KANNUR'

    KASARGOD = 'KASARGOD','KASARGOD'

class BatchChoices(models.TextChoices):

    PY_NOV_2024 = 'PY-NOV-2024','PY-NOV-2024'

    PY_JAN_2025 = 'PY-JAN-2025','PY-JAN-2025'

    DS_JAN_2025 = 'DS-JAN-2025','DS-JAN-2025'

    ST_JAN_2025 = 'ST-JAN-2025','ST-JAN-2025'

    MEARN_NOV_2024 = 'MEARN-NOV-2024','MEARN-NOV-2024'

    MEARN_JAN_2025 = 'MEARN-JAN-2025','MEARN-JAN-2025'

class TrainerChoices(models.TextChoices):

    JOHN_DOE = 'JOHN DOE','JOHN DOE'

    JAMES = 'JAMES','JAMES'

    PETER = 'PETER','PETER'

    ALEX = 'ALEX','ALEX'


class Students(BaseClass):

    '''
    personal details
    '''
    profile=models.OneToOneField('authentication.Profile',on_delete=models.CASCADE)

    first_name = models.CharField(max_length=50)

    last_name = models.CharField(max_length=50)

    email = models.EmailField(unique=True)

    photo = models.ImageField(upload_to='my_app')

    contact_num = models.CharField(max_length=50)

    house_name = models.CharField(max_length=25)

    post_office = models.CharField(max_length=25)

    district = models.CharField(max_length=20,choices=DistrictChoices.choices)

    pincode = models.CharField(max_length=6)

    '''
     course details

    '''

    adm_number = models.CharField(max_length=50)

    # course = models.CharField(max_length=25,choices=CourseChoices.choices)  # default = CourseChoices.PY_DJANGO

    course= models.ForeignKey('courses.Courses',null=True,on_delete=models.SET_NULL)

    # batch = models.CharField(max_length=50,choices=BatchChoices.choices)

    batch= models.ForeignKey('batches.Batches',null=True,on_delete=models.SET_NULL)

    # batch_date = models.DateField()

    join_date = models.DateField(auto_now_add=True) 

    # trainer_name = models.CharField(max_length=50,choices=TrainerChoices.choices)

    trainer=models.ForeignKey('trainers.Trainers',null=True,on_delete=models.SET_NULL)

    def __str__(self):

        return f'{self.first_name} {self.last_name}'

    class Meta:

        verbose_name ='Students'

        verbose_name_plural ='Students'

        ordering =['id']

    
