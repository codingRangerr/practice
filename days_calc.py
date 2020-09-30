days_of_month = {'jan': 31,
                 'feb': [28, 29],
                 'mar': 31,
                 'apr': 30,
                 'may': 31,
                 'jun': 30,
                 'jul': 31,
                 'aug': 31,
                 'sept': 30,
                 'oct': 31,
                 'nov': 30,
                 'dec': 31}


def is_leap_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def no_day(current_day, b_day):
    return
