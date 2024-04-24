from django.contrib import admin
from testapp.models import PuneJobs,HydJobs,BegrJobs
# Register your models here.
class PuneJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','address','email','phonenumber']
admin.site.register(PuneJobs,PuneJobsAdmin)


class HydJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','address','email','phonenumber']
admin.site.register(HydJobs,HydJobsAdmin)

class BegrJobsAdmin(admin.ModelAdmin):
     list_display = ['date','company','title','address','email','phonenumber']
admin.site.register(BegrJobs,BegrJobsAdmin)
