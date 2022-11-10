from django.http import HttpResponse
from django.shortcuts import render
import json


def chatbot(request):
    # 이거는 폴더 이름인듯 챗봇 폴더안의 html파일을 요청함
    return render(request,'chatbot/chatbot.html')

def chat_service(request):
    if request.method == 'POST':
        input1 = request.POST['input1']
        output = dict()
        output['response'] = "이건 응답"
        return HttpResponse(json.dumps(output),status=200)
    else:
        return render(request, 'chatbot/chatbot.html')