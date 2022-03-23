'''
서울대학교 학사일정(https://www.snu.ac.kr/academics/resources/calendar)을 크롤링하는 코드를 작성할 예정입니다.
'''
import requests
from bs4 import BeautifulSoup

url = "https://www.snu.ac.kr/academics/resources/calendar"

response = requests.get(url)

if response.status_code != 200:
    print(response.status_code)
    exit(0)

print(response.text)


