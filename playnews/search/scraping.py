# '키워드'를 입력해 저장된 json 파일에서 네이버에서 제공하는 기사일 경우에만 스크래핑한다.

# 단계 1: DB 연결 -> (희진 언니)
# 단계 2: org_link에 naver라는 키워드가 포함되어 있으면 스크래핑
#         아닐 경우 다음 요소로 넘어가기
# 단계 3: selenium을 이용하여 스크래핑 하기
import requests
from bs4 import beautifulSoup

header = {""} # User agent 정보
url = ''
res = requests.get(url, headers = header)
soup = beautifulSoup(res.text, 'html.parser')

if soup == None:
    print("soup가 리턴 받은 값 없음")

# 뉴스 본문 class="newsct_d=body"
    
# 뉴스 본문의 이미지와 텍스트를 순서로 어떻게 가져올 것 인가?

# 뉴스 내 이미지 추출

# 뉴스 내 텍스트 추출
# 1. 
# 2.
# 3.
