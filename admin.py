from django.contrib import admin
from .models import *


class display_custom_user(admin.ModelAdmin):
   list_display = ['username', 'user_type','email']

admin.site.register(Custom_user, display_custom_user)
admin.site.register(jobinformationModel)
admin.site.register(Jobseekermodel)
admin.site.register(RecruiterModel)

admin.site.register(recruiterContact)
admin.site.register(see_basic)
admin.site.register(seekerContact)
admin.site.register(re_basic)
admin.site.register(workexperience)
admin.site.register(Education_information)


