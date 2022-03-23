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
for month in months:
    monthval = month.select_one("span.month-text").get_text()
    print(monthval)
    events = month.select("div.work")
    for event in events:
        dayval = event.select_one("p.day").get_text()
        description = event.select_one("p.desc").get_text()
        print(dayval)
        print(description)




