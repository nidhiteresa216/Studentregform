from django.db import models

# Create your models here.
class Details(models.Model):
    first_name= models.CharField('Student First Name', max_length = 30)
    last_name= models.CharField('Student Last Name', max_length = 60)
    birth_date = models.DateField('Date of Birth', null = True, blank = True)
    phone=models.CharField('Contact',max_length = 12)
    email= models.EmailField('EmailID')
    address = models.CharField('Residence', max_length = 250)
    college_name = models.CharField('College Name', max_length = 100)
    course = models.CharField('Course Name', max_length = 50)
    about = models.TextField(blank = True)


    def __str__(self):
        return self.first_name + '' + self.last_name
        


