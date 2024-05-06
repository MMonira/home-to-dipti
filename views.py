from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from Job_portalapp.models import *
from django.contrib import messages
from PIL import Image


context = {
   'form_success': 'Signup done successfully',
   'form_warning': 'maybe password and confirm password didnt match',
   'usernameM': 'Username Already exists',
   'imagesize': 'Image size must be below than 300kb',
   'imageresolution': 'Image resolution must be eqal 500px',
   

}


def signuppage(request):
   if request.method == 'POST':
      uname = request.POST.get('username')
      paSSword = request.POST.get('password')
      CONfirmpassword = request.POST.get('confirm_password')
      first = request.POST.get('firstname')
      last = request.POST.get('lastname')
      age= request.POST.get('age')
      gender = request.POST.get('gender')
      city = request.POST.get('city')
      country = request.POST.get('country')
      user_type = request.POST.get('user_type')
      profile_photo = request.FILES.get('profile_photo')
      blood_group = request.POST.get('blood_group')
      
      usercheck = Custom_user.objects.filter(username = uname).exists()
      
      imagesixe = profile_photo.size
      
      requeredsize = 299 * 1024
      
      img = Image.open(profile_photo)

      w , h = img.size
      
      

      if usercheck:
         messages.error(request,context['usernameM'])

      elif requeredsize < imagesixe:
         messages.warning(request,context['imagesize'])

      elif w != 500  and h != 500 :
         messages.warning(request, context['imageresolution'])
         
      else:
         if paSSword == CONfirmpassword:
            user = Custom_user.objects.create_user(
               username = uname,
               password = paSSword,
               first_name = first,
               last_name = last,
               age = age,
               gender = gender,
               city = city,
               country = country,
               profile_photo = profile_photo,
               user_type = user_type,
               blood_group = blood_group,
            )
            
            if user_type == 'recruiter':
               RecruiterModel.objects.create(user = user)
            elif user_type == 'jobseeker':
               Jobseekermodel.objects.create(user = user)
               
            user.save()
            
            messages.success(request, context['form_success'])


            
            return redirect('signin')
         else:
            messages.warning(request,'Cannot signup maybe password didnt match')

            return redirect('signup')

   return render(request, 'signup.html')




def signinpage(request):
   if request.method == 'POST':
      uname = request.POST.get('username')
      paSSword = request.POST.get('password')
      
      user = authenticate (username = uname, password = paSSword)

      if user :
         login(request, user)
         return redirect('dashboard')
      else:
         messages.error(request,context['form_warning'])
         return redirect('signin')
         
   return render(request, 'signin.html')


@login_required
def dashboard(request):
   
   return render(request,'dashboard.html')


#all links

@login_required
def viewjoblist(request):
   current_user = request.user
   userType = request.user.user_type
   if userType == 'recruiter':
      infoo = jobinformationModel.objects.filter(created_by = current_user)
   else:
      infoo = jobinformationModel.objects.all()
   return render(request,'viewjoblist.html',{'info': infoo})


@login_required
def addjob(request):
   if request.method == 'POST':
      job_title = request.POST.get('job_title')
      job_description = request.POST.get('job_description')
      job_location = request.POST.get('job_location')
      deadline = request.POST.get('deadline')
      company_logo = request.FILES.get('company_logo')
      requirements = request.POST.get('requirements')
      qualifications = request.POST.get('qualifications')
      job_type = request.POST.get('job_type')
      work_place = request.POST.get('work_place')
      experience = request.POST.get('experience')
      salary = request.POST.get('salary')
      currentU = request.user
      data = jobinformationModel(
         job_title = job_title,
         job_description = job_description,
         job_location = job_location,
         deadline = deadline,
         company_logo = company_logo,
         requirements = requirements,
         qualifications = qualifications,
         job_type = job_type,
         work_place = work_place ,
         experience = experience,
         salary = salary ,
         created_by = currentU,
         
      )
      data.save()
      return redirect('viewjob')
   
   return render(request,'recruiter/addjob.html')



@login_required
def profile(request):
   current_user = request.user
   if request.user.user_type == 'recruiter':
      info = RecruiterModel.objects.get(user = current_user )
   else:
      info = Jobseekermodel.objects.get(user = current_user)


   return render(request,'profile.html',{'info':info})



@login_required
def second_profile(request):
   currentU = request.user
   usertype = request.user.user_type
   if usertype == 'recruiter' :
      info = RecruiterModel.objects.get(user = currentU)
   else:
      info = Jobseekermodel.objects.get(user = currentU)

   return render(request, 'second_profile.html',{'info':info})

   
@login_required
def secondeditprofile(request):
   
   return render(request,'secondeditprofile.html')
   


@login_required
def appliedjob(request):
   
   return render(request,'appliedjob.html')



@login_required
def logoutpage(request):
   logout(request)
   return redirect('signin')


@login_required
def editjob(request,myid):
   info = jobinformationModel.objects.get(id = myid)

   return render(request,'recruiter/editjob.html',{'info': info})



def updatepost(request):
   if request.method == 'POST':
      jid = request.POST.get('jid')
      job_title = request.POST.get('job_title')
      job_description = request.POST.get('job_description')
      job_location = request.POST.get('job_location')
      deadline = request.POST.get('deadline')
      company_logo = request.FILES.get('company_logo')
      precompany_logo = request.POST.get('precompany_logo')
      requirements = request.POST.get('requirements')
      qualifications = request.POST.get('qualifications')
      job_type = request.POST.get('job_type')
      work_place = request.POST.get('work_place')
      experience = request.POST.get('experience')
      salary = request.POST.get('salary')
      currentU = request.user
      data = jobinformationModel(
         id = jid,
         job_title = job_title,
         job_description = job_description,
         job_location = job_location,
         deadline = deadline,
         requirements = requirements,
         qualifications = qualifications,
         job_type = job_type,
         work_place = work_place ,
         experience = experience,
         salary = salary ,
         created_by = currentU,
         
      )
      
      if company_logo:
         data.company_logo = company_logo
         
      else:
         data.company_logo = precompany_logo
      
      data.save()
      return redirect('viewjob')


@login_required
def newpostview(request,myid):
   info = jobinformationModel.objects.get(id = myid)
   
   return render(request,'newpostview.html',{'info': info})


@login_required
def deletejob(request,myid):
   info = jobinformationModel.objects.get(id = myid)
   info.delete()
   return redirect('viewjob')

@login_required
def editprofile(request,myid):
   userType = request.user.user_type
   if userType == 'recruiter':
      info = RecruiterModel.objects.get(id = myid)
   else:
      info = Jobseekermodel.objects.get(id = myid)

   return render(request,'editprofile.html',{'info':info})

   

@login_required
def updateprofile(request):
   if request.method == 'POST':
      pid = request.POST.get('pid')
      uname = request.POST.get('username')
      paSSword = request.POST.get('password')
      CONfirmpassword = request.POST.get('confirm_password')
      first = request.POST.get('firstname')
      last = request.POST.get('lastname')
      age= request.POST.get('age')
      gender = request.POST.get('gender')
      city = request.POST.get('city')
      country = request.POST.get('country')
      user_type = request.POST.get('user_type')
      profile_photo = request.FILES.get('profile_photo')
      blood_group = request.POST.get('blood_group')
      preprofile_photo = request.POST.get('preprofile_photo')
      if user_type == "recruiter":
         recruiter_name = request.POST.get('recruiter_name')
         company_location = request.POST.get('company_location')
         company_name = request.POST.get('company_name')
      else :
         skills = request.POST.get('skills')
         experience = request.POST.get('experience')
         qualifications = request.POST.get('qualifications')   
         
      if paSSword == CONfirmpassword:
         user = Custom_user(
            id = pid,
            username = uname,
            password = paSSword,
            first_name = first,
            last_name = last,
            age = age,
            gender = gender,
            city = city,
            country = country,
            
            user_type = user_type,
            blood_group = blood_group,
         )
         if profile_photo :
            user.profile_photo = profile_photo
         else:
            user.profile_photo = preprofile_photo
            
         user.save()
      if user_type == "recruiter":
    
         
         recruiterdata = RecruiterModel(
            company_name = company_name,
            company_location = company_location,
            recruiter_name = recruiter_name,
         )
         recruiterdata.save()
         
      elif user_type == "jobseeker":

         seekerdata = Jobseekermodel(
            skills = skills,
            experience = experience,
            qualifications = qualifications,
         )
         seekerdata.save()
         return redirect('profile')

      else:
         return redirect('updateprofile')




      

      

@login_required
def selfpost(request ,myid):
   info = jobinformationModel.objects.filter(id = myid)

   return render(request,'selfpost.html',{'info': info})



@login_required
def seekercontact(request):
   
   return render(request, 'seekercontact.html')

   


@login_required
def wexperience(request):
   
   return render(request, 'wexperience.html')

   


@login_required
def education(request):
   
   return render(request, 'education.html')

   


@login_required
def seekerbasic(request):
   
   return render(request, 'seekerbasic.html')

   


@login_required
def recontact(request):
   
   return render(request, 'recontact.html')

   


@login_required
def recruiterbasic(request):
   
   return render(request, 'recruiterbasic.html')

   