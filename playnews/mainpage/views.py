from django.shortcuts import render # 기본 반환값 (템플릿 지정하는 함수)
from .models import UserInfo # 내가 만든 모델
from django.contrib import messages

from django.views.generic import View #클래스 뷰의 상위 클래스 (상속받기)
from django.http import HttpResponse # 직접 응답을 만들어서 전달할 때
from django.http import HttpResponseRedirect # 이미 만들어진 페이지로 이동
from django.contrib.auth import authenticate

def mainpage(request):
    # 해당 url이 오면 templates/mainpage/main.html을 보여주겠다.
    return render(request,'mainpage/mainpage.html')

def loginpage(request):
    return render(request,'mainpage/loginpage.html')

def loggedinpage(request):
    return render(request,'mainpage/loggedinpage.html')

def signuppage(request):
    return render(request,'mainpage/signuppage.html')





def login(request):
    id = request.POST.get('userid')
    pw = request.POST.get('userpw')
    infos = UserInfo.objects.all()
    for info in infos:
         if info.userid == id and info.userpw == pw:
              return render(request, 'mainpage/loggedinpage.html')
    return render(request,'mainpage/loginpage.html')

def signup(request):
    if 'checkid' in request.POST:
        id = request.POST.get('userid')
        infos = UserInfo.objects.all()
        for info in infos:
            if info.userid == id:
                messages.warning(request, "id가 중복되었습니다.")

            else:
                messages.warning(request, "사용 가능한 id 입니다.")

    elif 'signup' in request.POST:
        id = request.POST.get('userid')
        pw = request.POST.get('userpw')
        infos = UserInfo.objects.all()
        for info in infos:
            if info.userid == id and info.userpw == pw:
                return render(request, 'mainpage/loggedinpage.html')
    return render(request,'mainpage/loginpage.html')


# userid 와 userpw 가 db에 저장된것과 같은지 비교한후 일치하면 result.html로 간다.



