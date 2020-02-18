from django.contrib.auth import authenticate, login
from .models import User
from django.shortcuts import render, redirect

# Create your views here.

def st_login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request,"base.html")
        else:
            pass
        # 로그인 화면 보여주기
        pass
    elif request.method == 'POST':
        # 로그인 로직    
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            #로그인 확인 및 서비스 이동
            login(request, user)
            return redirect('projects:status')
        else:
            #로그인 실패 로그인 화면
            pass
    return render(request,'home.html')