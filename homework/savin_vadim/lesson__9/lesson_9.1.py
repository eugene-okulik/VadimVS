import datetime


origin_date = "Jan 15, 2023 - 12:05:33"
new_date = datetime.datetime.strptime(origin_date, "%b %d, %Y - %H:%M:%S")
print(datetime.datetime.strftime(new_date, "%B"))
print(datetime.datetime.strftime(new_date, "%d.%m.%Y, %H:%M"))
