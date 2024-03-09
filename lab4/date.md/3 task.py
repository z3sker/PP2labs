import datetime

cur_date = datetime.datetime.now()
cur_date_without_ms = datetime.datetime.now().replace(microsecond=0)

print("Current Datetome with ms   :", cur_date)
print("Current DateTime without ms:", cur_date_without_ms)