import os
import sys
# URL(대부분 HTTP)을 여는 데 도움이 되는 함수와 클래스를 정의한 라이브러리
import urllib.request
import datetime
import time
import json

# 클라이언트 ID/비밀키
client_id = 'IOUzsco6f11Y2fdiKzsh'
client_secret = 'pmfbtWIWhX'

#검색 결과를 JSON 형식으로 반환
url = 'https://openapi.naver.com/v1/search/news.json' 

# [url 접속]
def getRequestUrl(url):
    # class urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
    req = urllib.request.Request(url)

    # 헤더 객체를 이용해 헤더에 클라이언트 아이디, 비밀키 추가
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)
    
    try:
        response = urllib.request.urlopen(req)
        # 200 = OK, url 접속 성공
        if response.getcode() == 200:
            print("[%s]Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    
    # except 예외 처리 as 오류 메시지 변수
    except Exception as e :
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

# [네이버 뉴스 검색]
def getNaverSearch(node, srcText, start, display):
    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" % node
    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(srcText), start, display)

    url = base + node + parameters
    responseDecode = getRequestUrl(url)     #[CODE 1]

    if(responseDecode == None):
        return None
    else:
        return json.loads(responseDecode)

#[CODE 3]
def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']

    pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d, %b, %Y, %H:%M:%S+0900')
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

    jsonResult.append({'cnt':cnt, 'title':title, 'description':description,
                       'org_link':org_link, 'link':org_link, 'pDate':pDate})
    return

#[CODE 0]
def main():
    node = 'news'  #크롤링한 대상
    srcText = input('검색어를 입력하세요: ')
    cnt = 0
    jsonResult = []
    
    jsonResponse = getNaverSearch(node, srcText, 1, 100)  #[CODE 2]
    total = jsonResponse['total']
    
    while((jsonResponse != None) and (jsonResponse['display'] != 0)):
        for post in jsonResponse['items']:
            cnt+= 1
            getPostData(post, jsonResult, cnt)   #[CODE 3]
            
        start = jsonResponse['start'] + jsonResponse['display']
        jsonResponse = getNaverSearch(node, srcText, start, 100)   #[CODE 2]
        
    print('전체 검색 : %d 건' %total)
        
    with open('%s_naver_%s.json' % (srcText, node), 'w', encoding='utf8') as outfile:
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys = True, ensure_ascii = False)
            
        outfile.write(jsonFile)
            
    print("가져온 데이터 : %d 건" %(cnt))
    print('%s_naver_%s.json SAVED' % (srcText, node))

if __name__ == '__main__':
    main()                  