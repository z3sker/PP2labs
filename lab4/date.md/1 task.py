from datetime import datetime, timedelta

print("Current time: ", datetime.now())

print("5 days ago  : ", datetime.now() - timedelta(days= 5))