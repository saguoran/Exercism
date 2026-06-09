import calendar


def meetup_day(year, month, day, which):
    dict_days = {day: i for day, i in zip(calendar.day_name, range(7))}
    c = calendar.Calendar()
    dates = c.itermonthdates(year, month)
    days = [date for date in dates if date.weekday() == dict_days[day] and date.month == month]
    try:
        return days[int(which[0])-1]
    except ValueError:
        return days[-1] if which == 'last' else days[1] if days[1].day > 12 else days[2]
    except IndexError:
        raise MeetupDayException(r'.+')


class MeetupDayException(IndexError):
    def __init__(self, *args):
        IndexError.__init__(self, *args)

