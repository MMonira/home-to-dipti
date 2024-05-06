from django.db import models
from django.contrib.auth.models import AbstractUser

class Custom_user(AbstractUser):
   USER = [
      ('recruiter','recruiter'),('jobseeker','jobseeker')
   ]
   
   GENDER = [
      ('male','male'),('female','Female'),('other','Other')
   ]
   GROUP = [
      ('A+','A+'),('B+','B+'),('O+','O+'),('AB+','AB+')
   ]
   age = models.CharField(max_length=30)
   city = models.CharField(max_length=30)
   country = models.CharField(max_length=30)

   profile_photo = models.ImageField(upload_to='static/media')
   user_type = models.CharField(choices=USER , max_length=100)
   gender = models.CharField(choices=GENDER , max_length=100)
   blood_group = models.CharField(choices=GROUP , max_length=100, null=True)

class jobinformationModel(models.Model):
   TYPE = [
      ('full_time','full_time'),('part_time','part_time')
   ]
   PLACE = [
      ('remote','remote'),('on_site','on_site')
   ]
   job_title = models.CharField(max_length=100)
   salary = models.CharField(max_length=100)
   experience = models.CharField(max_length=100)
   requirements = models.CharField(max_length=100)
   qualifications = models.CharField(max_length=100)
   job_location = models.CharField(max_length=100)
   job_description = models.TextField()
   deadline = models.DateField()
   company_logo = models.ImageField(upload_to='static/media')
   job_type = models.CharField(choices=TYPE, max_length=100)
   work_place = models.CharField(choices=PLACE, max_length=100)
   created_by = models.ForeignKey(Custom_user, on_delete=models.CASCADE)
   
   def __str__(self):
      return self.job_title + ' ' + self.created_by.username
   
   
class RecruiterModel(models.Model):
   user = models.OneToOneField(Custom_user, on_delete=models.CASCADE , related_name='recruitermodel')
   company_name = models.CharField(max_length=100)
   company_location = models.CharField(max_length=100)
   recruiter_name = models.CharField(max_length=100)

   def __str__(self):
      return self.recruiter_name + ' '+ self.user.email
   
   
class Jobseekermodel(models.Model):
   QUALIFICATIONS = [
      ('hsc','HSC'),('diploma','Diploma'),('honurs','Honours'),('masters','Masters')
   ]
   user = models.OneToOneField(Custom_user, on_delete=models.CASCADE, related_name='seekermodel')
   qualifications = models.CharField(choices=QUALIFICATIONS , max_length=100, null= True)
   experience = models.CharField(max_length=100)
   skills = models.CharField(max_length=100)
   
   def __str__(self):
      return self.skills + ' '+ self.user.first_name
   
class re_basic(models.Model):
   user = models.OneToOneField(Custom_user, on_delete=models.CASCADE, related_name= 'reruiter_basic')
   fathersname = models.CharField(max_length=100)
   ma = models.CharField(max_length=100)
   preaddress = models.CharField(max_length=100)
   
class see_basic(models.Model):
   user = models.OneToOneField(Custom_user, on_delete=models.CASCADE,related_name= 'seeker_basic')
   fathersname = models.CharField(max_length=100)
   ma = models.CharField(max_length=100)
   preaddress = models.CharField(max_length=100)
   
class seekerContact (models.Model):
   user = models.OneToOneField(Custom_user, on_delete=models.CASCADE, related_name='seecontact')
   phone = models.CharField(max_length=100)
   email = models.CharField(max_length=100)
   instragram = models.CharField(max_length=100)
   
class recruiterContact (models.Model):
   user = models.OneToOneField(Custom_user, on_delete=models.CASCADE, related_name='recontact')
   phone = models.CharField(max_length=100)
   email = models.CharField(max_length=100)
   instragram = models.CharField(max_length=100)
   
   
class Education_information(models.Model):
   user = models.OneToOneField(Custom_user, on_delete=models.CASCADE , related_name='education')
   last_education = models.CharField(max_length=200)
   gpa = models.CharField(max_length=200)
   certificate = models.CharField(max_length=200)

   
   
class workexperience(models.Model):
   user = models.OneToOneField(Custom_user, on_delete=models.CASCADE , related_name='workexperience')
   computer = models.CharField(max_length=200)
   institute = models.CharField(max_length=200)
   designation = models.CharField(max_length=200)

   