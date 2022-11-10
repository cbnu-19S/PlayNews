from django.urls import path

from . import views

# 패스에 따라 (url에 따라) 뷰 안의 챗봇이라는 함수를 호출함
urlpatterns = [
    path('', views.chatbot, name='go_chatbot'),
    path('chat_service/', views.chat_service),
    ]