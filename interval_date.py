from datetime import date, timedelta, datetime
import calendar


def all_sat_btw_dates(start_date, end_date):
    """
    To get list of dates which are saturday and between given dates
    :param start_date: start date in datetime.date format
    :param end_date: end date in datetime.date format
    :return: list of dates (only saturdays)
    """
    delta = end_date - start_date
    saturdays = []
    for i in range(delta.days + 1):
        next_date = start_date + timedelta(days=i)
        if next_date.isoweekday() == 6:
            saturdays.append(next_date)
    return saturdays


def is_4th_sat(dt):
    """
    To find the give date is 4th saturday or not
    :param dt: date in datetime.date format
    :return: True is 4th sat / False if not
    """
    month = dt.month
    year = dt.year
    month_range = calendar.monthrange(year, month)
    all_sat = all_sat_btw_dates(date(year, month, 1), date(year, month, month_range[1]))
    return dt == all_sat[3]


def get_interval_dates(start_date_str, end_date_str):
    """
    Prints dates line by line which are saturday and multiple of 5 or 4th of saturday
    :param start_date_str: start date in string
    :param end_date_str: end date in string (inclusive date)
    :return: None (prints result dates line by line)
    """
    if type(start_date_str) != str or type(end_date_str) != str:
        print("Invalid input type, must be string")
        return

    start_date = datetime.strptime(start_date_str, '%Y%m%d').date()
    end_date = datetime.strptime(end_date_str, '%Y%m%d').date()

    if (start_date < date(1900, 1, 1)) or (start_date > date(2100, 12, 31)) or \
            (end_date < date(1900, 1, 1)) or (end_date > date(2100, 12, 31)):
        print("Invalid date range")
        return

    if start_date > end_date:
        print("end date must be greater than start date")
        return
    
    res = []
    for sat in all_sat_btw_dates(start_date, end_date):
        if sat.day % 5 == 0:
            res.append(sat)
        if is_4th_sat(sat):
            if sat in res:
                res.remove(sat)
            else:
                res.append(sat)

    for r in res:
        r = r.strftime("%Y%m%d")
        print(r)


if __name__ == "__main__":
    input_start_date = "20180728"
    input_end_date = "20180927"

    get_interval_dates(input_start_date, input_end_date)
