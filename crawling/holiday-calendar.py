"""
Google에서 제공하는 iCalendar로부터 한국 공휴일 가져오는 코드를 작성할 예정입니다.
"""

from icalendar import Calendar
import requests

# Parse the URL
url = "https://calendar.google.com/calendar/ical/ko.south_korea%23holiday%40group.v.calendar.google.com/public/basic.ics"
cal = Calendar.from_ical(requests.get(url).text)

for component in cal.walk("VEVENT"):
    if component["DESCRIPTION"].to_ical().decode("utf-8") == u"공휴일":
        dt_start = component["DTSTART"].to_ical().decode("utf-8")
        dt_end = component["DTEND"].to_ical().decode("utf-8")

        print(
            component["SUMMARY"].to_ical().decode("utf-8"),
            dt_start,
            dt_end,
            sep="\t",
        )
