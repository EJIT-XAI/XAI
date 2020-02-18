from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/')
def statuspage(request):
    return render(request,'statuspage.html')

@login_required(login_url='/')
def loaddata(request):
    return render(request,'loaddata.html')

@login_required(login_url='/')
def edapage(request):
    return render(request,'edapage.html')


@login_required(login_url='/')
def automl(request):
    return render(request,'automl.html')


@login_required(login_url='/')
def modelcreate(request):
    return render(request,'modelcreate.html')


@login_required(login_url='/')
def xai(request):
    return render(request,'xai.html')