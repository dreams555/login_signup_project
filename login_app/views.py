from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

#로그인 기능 구현
def login(request):
    #로그인 됐을때
    if request.method == 'POST':
       username = request.POST['ID']
       password = request.POST['PW']
       user = auth.authenticate(request, username=username, password=password)
       print(user)
       if user is not None:
           auth.login(request, user)
           return redirect('home')
        # 로그인 안됐을때(사전형 자료형 사용)
       else: 
           #login.html에 에러 키값 입력해줘야함
            context = {'error':'존재하지 않는 회원입니다.'}
            return render(request, 'login.html', context)

#home에서 로그인페이지로 갈때 사용(home.html참고)
    elif request.method == 'GET':
        return render(request, 'login.html')

#로그인이 되어 있을 때만 실행 psst방식 굳이사용안해도 됨
@login_required
def logout(request):
    auth.logout(request)
    return redirect('home')