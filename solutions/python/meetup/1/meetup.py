from datetime import date
from calendar import Calendar

keywords = ['1st', '2nd', '3rd', '4th', 'last', 'teenth']
days = {'Sunday': 6, 'Monday': 0, 'Tuesday': 1, 'Wednesday': 2,
        'Thursday': 3, 'Friday': 4, 'Saturday': 5}
whichs = {
    '1st': (lambda x: x[0:7]),
    '2nd': (lambda x: x[7:14]),
    '3rd': (lambda x: x[14:21]),
    '4th': (lambda x: x[21:28]),
    '5th': (lambda x: x[28:]),
    'last': (lambda x: x[-7:]),
    'teenth': (lambda x: x[12:19])
}

def meetup_day(year, month, day_of_the_week, which):
    cal = Calendar(6).itermonthdays2(year, month)
    cal = list(filter(lambda x: x[0] != 0, cal))
    try:
        _date, _day = list(filter(
            lambda x: x[1] == days[day_of_the_week], whichs[which](cal)))[0]
        return date(year, month, _date)
    except IndexError:
        raise MeetupDayException(r'.+')


class MeetupDayException(Exception):
    def __init__(self, message):
        super().__init__(message)

