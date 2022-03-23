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

html = response.text
soup = BeautifulSoup(html, "html.parser")
calendar = soup.select_one("div.calendar-wrap")
months = calendar.select("div.work-wrap")
print(months[0])


