'''
서울대학교 학사일정(https://www.snu.ac.kr/academics/resources/calendar)을 크롤링하는 코드를 작성할 예정입니다.
'''
import requests
from bs4 import BeautifulSoup
import re

korean = re.compile('[\u3131-\u3163\uac00-\ud7a3]+')
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
    parsemonth = re.sub(korean, '', monthval)
    yearmonth = parsemonth.split()
    if len(yearmonth) == 1:
        yearstr = "2022"
        monthstr = yearmonth[0]
    else:
        yearstr = yearmonth[0]
        monthstr = yearmonth[1]
    events = month.select("div.work")
    for event in events:
        dayval = event.select_one("p.day").get_text()
        description = event.select_one("p.desc").get_text()
        parseday = re.sub("\.", " ", re.sub("\(\)", '', re.sub(korean , '', dayval)))
        startyearstr = yearstr
        endyearstr = yearstr
        startmonthstr = monthstr
        endmonthstr = monthstr
        if "~" in parseday:
            startdaystr, end = parseday.split("~")
            endsplit = end.split()
            if len(endsplit) == 1:
                enddaystr = endsplit[0]
            elif len(endsplit) == 2:
                endmonthstr = endsplit[0]
                enddaystr = endsplit[1]
            else:
                endyearstr = endsplit[0]
                endmonthstr = endsplit[1]
                enddaystr = endsplit[2]
        else:
            startdaystr = parseday
            enddaystr = parseday

        print(startyearstr + "-" + startmonthstr + "-" + startdaystr)
        print(endyearstr + "-" + endmonthstr + "-" + enddaystr)
        print(description)




