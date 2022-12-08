from django.http import HttpResponse
from django.shortcuts import render
import json


def chatbot(request):
    return render(request,'chatbot/chatbot.html')

def chat_service(request):
    if request.method == 'POST':
        input1 = request.POST['input1']
        output = dict()
        output['response'] = "이건 응답"
        return HttpResponse(json.dumps(output),status=200)
    else:
        return render(request, 'chatbot/chatbot.html')