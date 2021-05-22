from django.contrib import admin
from .models import Profile, Work, Experience, Education, Software, Technical

admin.site.register(Profile)
admin.site.register(Work)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Software)
admin.site.register(Technical)