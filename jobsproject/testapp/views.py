from django.shortcuts import render
from testapp.models import HydJobs,PuneJobs,BegrJobs
# Create your views here.
def index(request):
    return render(request, 'testapp/index.html')

def Hydjobs(request):
    my_list=HydJobs.objects.all()
    return render(request, 'testapp/hydjobs.html',{'my_list': my_list})

def Punejobs(request):
    my_list=PuneJobs.objects.all()
    return render(request,'testapp/punejobs.html',{'my_list':my_list})

def Benjobs(request):
    my_list=BegrJobs.objects.all()
    return render(request,'testapp/bngjobs.html',{'my_list':my_list})