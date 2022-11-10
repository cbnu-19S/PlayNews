from django.urls import path, include

# 현재 같은 폴더 레벨의 뷰를 임폴트 하겠다.
from . import views

# 여기서 name은 html에 들어가는 url의 별명
# 해당 path의 url이 들어오면 뷰에있는 main이라는 함수를 실행하겠다.
urlpatterns = [

    path('', views.mainpage, name='go_mainpage'),
    path('loginpage/', views.loginpage, name='go_loginpage'),
    path('loggedin/', views.loggedinpage, name='go_loggedinpage'),
    path('login/', views.login, name='login'),
    path('signuppage/', views.signuppage, name='go_signuppage'),
    path('signup/', views.signup, name='signup'),

    ]

#url을 타고 들어간다음에 url에 따라 어떤 view를 보여줄지 선택한다.