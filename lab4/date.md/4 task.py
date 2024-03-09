from datetime import datetime, time

def dif_in_sec(date1, date2):
    delta = date1 - date2
    return delta.days * 24 * 3600 + delta.seconds

date1 = datetime.now()
date2 = datetime.strptime('2024-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')

print(dif_in_sec(date1, date2))