# 알고리즘
# 1. API랑 통신해서 naver link만 가져오기 -> 완료??!
# 2. 데이터테이블에 맞춰서 데이터 스크래핑하기!

# https://velog.io/@lybin10/%EB%84%A4%EC%9D%B4%EB%B2%84-API%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%ED%81%AC%EB%A1%A4%EB%A7%81

# 추가로 상의할 부분!
# 키워드 -> 언니가 데이터베이스에 저장하기 위해 따로 코드 작성하면 될 듯함
# 기사 중간중간 프레임워크나 데이터베이스 관련된 코드가 삽입되어 있어서 텍스트 그래도 가져와야 할 것 같음
# br 태그만 그대로 가져오면 될 듯함
# DB 속성 중 '전화' 삭제하기 (기사에 있는 걸 본 적이 없음...), 기자이름이랑 메일 같이 표시되도록 바꾸기!

# --------------------------------------------------------------------------
# URL(대부분 HTTP)을 여는 데 도움이 되는 함수와 클래스를 정의한 라이브러리
import urllib.request
import json
import datetime
from bs4 import BeautifulSoup, Comment
from requests import get
import pickle

# 네이버 클라이언트 ID/비밀키
client_id = 'IOUzsco6f11Y2fdiKzsh'
client_secret = 'pmfbtWIWhX'

# Api URL
news_api = "https://openapi.naver.com/v1/search/news.json"
url_news = "https://openapi.naver.com/v1/search"

# [CODE 1] - 서버에 요청해 받은 json 파일을 python의 str 타입으로 변환시켜 반환
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

# [CODE 2] 
def getNaverSearch(type, srcText, start, display):
    type = "/%s.json" % type

    # API를 호출할 때는 검색어와 검색 조건을 쿼리 스트링(Query String) 형식의 데이터로 전달

    # urllib.parse.quote(string, safe='/', encoding=None, errors=None)
    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(srcText), start, display)

    url = url_news + type + parameters
    responseDecode = getRequestUrl(url)     #[CODE 1]

    # try:
    if(responseDecode == None):
        return None

    else:
        return json.loads(responseDecode) # JSON 문서를 포함하는 str -> 파이썬 객체로 변환(여기서는 dict, 어떤 형식으로 변환되는지는 json.loads() 변환표 참고)
    
#[CODE 3] - str 구분해서 저장하기
def getPostData(post, jsonResult, cnt):
    link = post['link'] #네이버 뉴스 URL
    title = post['title'] # 기사 제목
    jsonResult.append({'cnt':cnt, 'title':title, 'link':link})
    return


# find_all() -> list
# [CODE 4] - parse html
def getNewsData(post, DataResult):
    # 기존 정보 넣기
    cnt = post['cnt']
    title = post['title']
    link = post['link']
    
    # bs4 이용하여 스크래핑하는 코드 👇 headers에 꼭 접속 정보 넣어 줘야 함
    response = get(post['link'], headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'})
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 기사 작성 날짜 [Date]
    date_first = soup.find('span', class_='media_end_head_info_datestamp_time _ARTICLE_DATE_TIME')
    date_mod = soup.find('span', class_='media_end_head_info_datestamp_time _ARTICLE_MODIFY_DATE_TIME _ARTICLE_DATE_TIME')
    
    # 신문사 [newspaper]
    newspaper = soup.find('img', class_='media_end_head_top_logo_img light_type', alt = True)
    newspaper = newspaper['alt']
    
    # 기자 이름 [writer]
    writer = soup.find('em', class_="media_end_head_journalist_name")
    if writer is None:
        writer = soup.find('span', class_="byline_s")

    # 수정
    body = soup.find('div', class_="go_trans _article_content")
    
    # 알고리즘 
    # 본문 for문을 돌면서 img 태그는 이미지에 따로 저장, 텍스트는 텍스트 리스트에 따로 저장
    # 이미지가 나오기 전까지 문장들을 붙여서 저장하다가 이미지가 나오면 바로 리스트에 저장, 그리고 다음 텍스트들은 다음 인덱스에 넣는다.
    # 이미지가 나오면 img 링크와 설명을 따로 저장한다. (태그 삭제하고 넣어버리기)
    context = [] # 본문 내용
    img_link = [] # 이미지 링크
    img_alt = [] # 이미지 설명
    content = ''
    
    for i in body:
        if (i.find('img') == -1) or(i.find('img') == None) and (i.find('em') == -1) or(i.find('em') == None):
            content += i.text
        else:
            if i.find('img') is not None:
                img = i.find('img')
                img_link.append(img['data-src'])
                alt = i.find('em', class_ = 'img_desc')
                img_alt.append(alt.text)
                context.append(content)
                content = ''
            else:
                continue
                
    if date_mod is not None and writer is not None:
        DataResult.append({'cnt':cnt, 'title' : title, 'link' : link , 'date_first' : date_first.string, 'date_mod' : date_mod.string, 'newspaper':newspaper, 'writer':writer.string, 'context':context, 'img':
        {
            'img_link':img_link,
            'img_alt':img_alt
        }
            })
    elif date_mod is None and writer is not None:
         DataResult.append({'cnt':cnt, 'title' : title, 'link' : link , 'date_first' : date_first.string, 'date_mod' : None, 'newspaper':newspaper, 'writer':writer.string, 'context':context, 'img':
        {
            'img_link':img_link,
            'img_alt':img_alt
        }
            })
    elif date_mod is not None and writer is None:
         DataResult.append({'cnt':cnt, 'title' : title, 'link' : link , 'date_first' : date_first.string, 'date_mod' : date_mod.string, 'newspaper':newspaper, 'writer':None, 'context':context, 'img':
        {
            'img_link':img_link,
            'img_alt':img_alt
        }
            })
    else:
        DataResult.append({'cnt':cnt, 'title' : title, 'link' : link , 'date_first' : date_first.string, 'date_mod' : None, 'newspaper':newspaper, 'writer':None, 'context':context, 'img':
        {
            'img_link':img_link,
            'img_alt':img_alt
        }
            })
        
    print(DataResult)
    return

#[CODE 0] - main 함수
def main():
    type = 'news'  # 검색-뉴스를 알려 주기 위한 변수
    keyword = input('검색어를 입력하세요: ') # 검색어 입력
    cnt = 0
    jsonResult = [] # 반환된 json 파일을 저장할 변수
    
    jsonResponse = getNaverSearch(type, keyword, 1, 100)  #[CODE 2], start = 1, display = 100.
    
    if((jsonResponse != None) and (jsonResponse['display'] != 0)):
        for post in jsonResponse['items']:
            if ("n.news.naver.com" in post['link'] and cnt < 10): # 링크가 네이버 뉴스 기사일 때만 스크래핑
                cnt+= 1
                getPostData(post, jsonResult, cnt)   #[CODE 3]
    
    DataResult = [] # 네이버의 기사 스크래핑 데이터와 jsonResponse에 있던 데이터들을 병합하여 저장할 리스트
    if ((jsonResult != None)):
        for post in jsonResult:
            if (cnt > 0):    
                getNewsData(post, DataResult)
                cnt -= 1;

if __name__ == '__main__':
    main()