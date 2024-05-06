
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signinpage,name='signin'),
    path('signup/', signuppage,name='signup'),
    path('dashboard/', dashboard,name='dashboard'),
    
    
    path('addjob/',addjob,name='addjob'),
    path('viewjob/',viewjoblist,name='viewjob'),
    path('appliedjob/',appliedjob,name='appliedjob'),
    path('profile/',profile,name='profile'),
    path('second_profile/',second_profile,name='second_profile'),
    path('logout/',logoutpage,name='logout'),
    
    
    
    path('edit/<str:myid>',editjob,name='edit'),
    path('delete/<str:myid>',deletejob,name='delete'),
    path('view/<str:myid>',newpostview,name='view'),
    path('update/',updatepost,name='update'),
    
    
    
    path('updateprofile/',updateprofile,name='updateprofile'),
    path('editprofile/<str:myid>',editprofile,name='editprofile'),
    path('selfpost/<str:myid>',selfpost,name='selfpost'),
    
    
    
    
    path('profile/seekercontact/',seekercontact,name='seekercontact'),
    path('profile/wexperience/',wexperience,name='wexperience'),
    path('profile/education/',education,name='education'),
    path('profile/seekerbasic/',seekerbasic,name='seekerbasic'),
    path('profile/recontact/',recontact,name='recontact'),
    path('profile/recruiterbasic/',recruiterbasic,name='recruiterbasic'),
    path('profile/secondeditprofile/',secondeditprofile,name='secondeditprofile'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
