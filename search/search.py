# URL(대부분 HTTP)을 여는 데 도움이 되는 함수와 클래스를 정의한 라이브러리
import urllib.request
import json
import datetime

# 클라이언트 ID/비밀키
client_id = 'IOUzsco6f11Y2fdiKzsh'
client_secret = 'pmfbtWIWhX'

# Api URL
news_api = 'https://openapi.naver.com/v1/search/news.json'
error_api = 'https://openapi.naver.com/v1/search/errata.json'

# 
url_news = "https://openapi.naver.com/v1/search"

def getRequestUrl(api_url):
    # class urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
    req = urllib.request.Request(api_url)

    # 헤더 객체를 이용해 헤더에 클라이언트 아이디, 비밀키 추가
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)
    
    try:
        response = urllib.request.urlopen(req)
        # 200 = OK, news_api 접속 성공
        if response.getcode() == 200:
            print(f"{datetime.datetime.now()}: {api_url} Request Success")
            return response.read().decode('utf-8')
    
    # except 예외 처리 as 오류 메시지 변수
    except Exception as e :
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), api_url))
        return None

# [CODE 1] - 서버에 요청해 받은 json 파일을 python str 타입으로 변환시켜 반환

def getNaverSearch(type, srcText, start, display):
    type = "/%s.json" % type

    # API를 호출할 때는 검색어와 검색 조건을 쿼리 스트링(Query String) 형식의 데이터로 전달합니다.

    # urllib.parse.quote(string, safe='/', encoding=None, errors=None)
    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(srcText), start, display)

    url = url_news + type + parameters
    responseDecode = getRequestUrl(url)     #[CODE 1]

    # try:
    if(responseDecode == None):
        return None

    # elif (responseDecode.):
    #     # 오타 변환

    else:
        return json.loads(responseDecode) # JSON 문서를 포함하는 str -> 파이썬 객체로 변환(여기서는 dict, 어떤 형식으로 변환되는지는 json.loads() 변환표 참고)
    
#[CODE 3] - 
def getPostData(post, jsonResult, cnt):
    title = post['title']
    link = post['link'] #네이버 뉴스 URL, 네이버에 제공된 기사 아니면 원문 URL 반환
    pDate = post['pubDate']

    jsonResult.append({'cnt':cnt, 'title':title,
                       'link':link, 'pDate':pDate})
    return

#[CODE 0] - main 함수
def main():
    type = 'news'  # 검색-뉴스를 알려 주기 위한 변수
    keyword = input('검색어를 입력하세요: ') # 검색어 입력
    cnt = 0
    jsonResult = [] # 반환된 json 파일을 저장할 변수
    
    jsonResponse = getNaverSearch(type, keyword, 1, 100)  #[CODE 2], start = 1, display = 100.
    total = jsonResponse['total']
    
    # jsonResponse(검색 결과)에 데이터가 있을 때 for문으로 검색 결과를 한 개씩 처리하는 작업 반복
    if((jsonResponse != None) and (jsonResponse['display'] != 0)):


        for post in jsonResponse['items']:
            cnt+= 1
            getPostData(post, jsonResult, cnt)   #[CODE 3]

        # 반복 작업이 끝나면 다음 검색 결과를 가져옴
        # start = jsonResponse['start'] + jsonResponse['display']
        # jsonResponse = getNaverSearch(keyword, srcText, start, 20)   #[CODE 2]
        
    print('전체 검색 : %d 건' %total)
    
    # json 파일 객체 생성
    # with문 -> 파일 열고 닫는 것을 자동으로 처리해 줌
    # with open("foo.txt", "w") as f:
    # with open('%s_naver_%s.json' % (srcText, keyword), 'w', encoding='utf8') as outfile:
    #     # 예쁜 인쇄(^ㅅ^ ㅋㅋ)로 정렬
    #     jsonFile = json.dumps(jsonResult, indent=4, sort_keys = True, ensure_ascii = False) 
    # json.dumps -> dic -> json 형식으로 변환
        
    #     # 파일 작성
    #     outfile.write(jsonFile)
    print("가져온 데이터 : %d 건" %(cnt))

if __name__ == '__main__':
    main()                  