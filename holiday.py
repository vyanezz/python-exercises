from datetime import datetime, timedelta
import holidays


def check_workdays(num_dates_wo_weekends, num_holidays):
    workdays = num_dates_wo_weekends - num_holidays
    print("Number or workdays (w/o Holidays) between the two dates: ", workdays)


def check_holidays(dates, city, num_dates_wo_weekends):
    festivos = holidays.country_holidays("ES", subdiv=city)
    num_holidays = 0
    for date in dates:
        if date in festivos:
            num_holidays += 1
    print("Holidays between the two dates in Spanish format: ", num_holidays)

    return check_workdays(num_dates_wo_weekends, num_holidays)


def check_total_days(start_date, end_date, city):
    diferencia = end_date - start_date
    num_dias = diferencia.days
    print("Number of total days between two dates: ", num_dias)
    dates = []
    for i in range(num_dias + 1):
        date = start_date + timedelta(days=i)
        dates.append(date)

    return check_days_wo_weekends(dates, city)


def check_days_wo_weekends(dates, city):
    num_dates_wo_weekends = 0
    for date in dates:
        if date.strftime('%A') != "Saturday" and date.strftime('%A') != "Sunday":
            num_dates_wo_weekends += 1
    print("Number or workdays (w/o Weekends) between the two dates: ", num_dates_wo_weekends)
    return check_holidays(dates, city, num_dates_wo_weekends)


date_from_str = input("Ingresa fecha inicio (YYYY-MM-DD): ")
date_to_str = input("Ingresa fecha fin (YYYY-MM-DD): ")
ca = input("Ingresa comunidad Autonoma: ")
start_date = datetime.strptime(date_from_str, "%Y-%m-%d")
end_date = datetime.strptime(date_to_str, "%Y-%m-%d")
check_total_days(start_date, end_date, ca)
