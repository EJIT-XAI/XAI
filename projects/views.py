from django.shortcuts import render, redirect


# Create your views here.
def statuspage(request):
    return render(request,'statuspage.html')


def dataload(request):
    return render(request,'dataload.html')

def edapage(request):
    return render(request,'edapage.html')

def automl(request):
    return render(request,'automl.html')

def modelcreate(request):
    return render(request,'modelcreate.html')

def xai(request):
    return render(request,'xai.html')