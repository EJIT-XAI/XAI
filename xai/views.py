from django.shortcuts import render
from django.http import HttpResponse


from module.monitor import get_statistics
# Create your views here.
def main(request):
    statistics=get_statistics()
    print(statistics)
    return render(request, 'dashboard.html')
