"""
This module contains utility functions.

"""
# get the current date from the user
    # ensures that i always have the same format for dates
def get_date():
    year = int(input("Year: "))
    month = int(input("Month (1-12)?: "))
    day = int(input("Day (1-31)?: "))
    return (year, month, day)

# check if the start date is before the end date
def check_dates(start_date, end_date):
    start_year, start_month, start_day = start_date
    end_year, end_month, end_day = end_date
    if start_year > end_year or (start_year == end_year and start_month > end_month) or (start_year == end_year and start_month == end_month and start_day > end_day):
        return False
    return True

# format the date as "YYYY-MM-DD" to be displayed
def get_format_date(date):
    (year, month, day) = date
    return f"{year}-{month}-{day}"

# check if a year is a leap year
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# calculate the number of days in a month, given the year and month
def days_in_a_month(year, month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap_year(year):
        return 29
    return days_in_month[month - 1]

# calculate the number of days passed since the start of the year
def days_from_start_of_year(year, month, day):
    total_days = 0
    for m in range(1, month):
        total_days += days_in_a_month(year, m)
    total_days += day
    return total_days

# calculate the number of days until the festival date, given the current date and the festival date
def calculate_days_until_festival(current_date, festival_date):
    current_year, current_month, current_day = current_date
    festival_year, festival_month, festival_day = festival_date

    # calculate days in the current year from current date to end of the year
    days_in_current_year = (366 if is_leap_year(current_year) else 365)
    days_passed_current_year = days_from_start_of_year(current_year, current_month, current_day)
    remaining_days_current_year = days_in_current_year - days_passed_current_year

    # calculate days from the start of the festival year to the festival date
    days_up_to_festival = days_from_start_of_year(festival_year, festival_month, festival_day)

    total_days = 0

    # case 1:  festival is in the same year
    if current_year == festival_year:
        total_days = days_up_to_festival - days_passed_current_year
    # case 2:  festival is in a future year
    elif current_year < festival_year:
        total_days = remaining_days_current_year + days_up_to_festival
        # add full years
        for year in range(current_year + 1, festival_year):
            total_days += 366 if is_leap_year(year) else 365
    # case 3: festival date is earlier than the current date
    else:
        total_days = -1 

    return total_days