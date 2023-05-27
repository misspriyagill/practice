def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "true"
            else:
                return "False"
        else:
            return "true"
    else:
        return "False"


def days_in_month(year_value, month_value):
    month_days_non_leap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_days_leap = [31, 29, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
    if is_leap(year_value) == "true":
        print(month_days_leap[month_value - 1])
    else:
        print(month_days_non_leap[month_value - 1])

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))

days_in_month(year, month)
