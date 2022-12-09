from django.shortcuts import render # 기본 반환값 (템플릿 지정하는 함수)
from .models import Userinfo, Newsinfo # 내가 만든 모델
from django.contrib import messages

from django.views.generic import View #클래스 뷰의 상위 클래스 (상속받기)
from django.http import HttpResponse # 직접 응답을 만들어서 전달할 때
from django.http import HttpResponseRedirect # 이미 만들어진 페이지로 이동
from django.contrib.auth import authenticate






def mainpage(request):
    newsinfos=Newsinfo.objects.all()

    news_keyword_list = []
    news_firm_list = []
    for newsinfo in newsinfos:
        if newsinfo.newspaper not in news_firm_list:
            news_firm_list.append(newsinfo.newspaper)

    for newsinfo in newsinfos:
        if newsinfo.keyword not in news_keyword_list:
            news_keyword_list.append(newsinfo.keyword)

    # 해당 url이 오면 templates/mainpage/main.html을 보여주겠다.
    return render(request,'mainpage/mainpage.html',{'newsinfos':newsinfos,'news_firm_list':news_firm_list,'news_keyword_list':news_keyword_list})

def news_firm(requset,firm):
    newsinfos_firm = Newsinfo.objects.filter(newspaper=firm)
    return render(requset,'mainpage/news_firm.html', {'newsinfos_firm':newsinfos_firm})


def article(request,id):
    article=Newsinfo.objects.get(newsid=id)
    return render(request, 'mainpage/article.html',{'article':article})

def loginpage(request):
    return render(request,'mainpage/loginpage.html')

def loggedinpage(request):
    return render(request,'mainpage/loggedinpage.html')

def signuppage(request):
    return render(request,'mainpage/signuppage.html')




def login(request):
    id = request.POST.get('userid')
    pw = request.POST.get('userpw')
    infos = Userinfo.objects.all()
    for info in infos:
         if info.userid == id and info.userpw == pw:
              return render(request, 'mainpage/loggedinpage.html')
    return render(request,'mainpage/loginpage.html')



def signup2(request):
    if 'checkid' in request.POST:
        id = request.POST.get('userid')
        infos = Userinfo.objects.all()
        is_exist = False
        for info in infos:
            if info.userid == id:
                messages.add_message(request, messages.ERROR, 'id가 중복되었습니다.')
                is_exist = True
            else:
                messages.add_message(request, messages.SUCCESS, '사용 가능한 id 입니다.')
        return render(request,'mainpage/signuppage.html')
    elif 'signup' in request.POST:
        Userinfo.objects.create(
            userid=request.POST.get('userid'),
            userpw=request.POST.get('userpw'),
            username=request.POST.get('username'),
            useremail=request.POST.get('useremail'),
            # userAddress=request.POST.get('useraddress'),
            userPhone=request.POST.get('userphone'),
         )
        return render(request,'mainpage/loginpage.html')






def check(request):
    id = request.POST.get('userid')
    infos = Userinfo.objects.all()
    for info in infos:
        if info.userid == id:
            return HttpResponse("id가 중복되었습니다.")
    return HttpResponse("사용가능한 id 입니다.")


def signup(request):
    if request.method == 'POST':
        Userinfo.objects.create(
            userid=request.POST.get('userid'),
            userpw=request.POST.get('userpw'),
            username=request.POST.get('username'),
            useremail=request.POST.get('useremail'),
            # userAddress=request.POST.get('userAddress'),
            userphone=request.POST.get('userPhone'),
        )
    return render(request, 'mainpage/loginpage.html')

# userid 와 userpw 가 db에 저장된것과 같은지 비교한후 일치하면 result.html로 간다.



