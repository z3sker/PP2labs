# Python Datetime

# Dates in Python are handled using the datetime module.

# Example: Importing the datetime module and displaying the current date
import datetime

x = datetime.datetime.now()
print(x)

# Date Output
# Dates contain year, month, day, hour, minute, second, and microsecond

# Example: Returning the year and name of the weekday
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

# Creating Date Objects
# Date objects are created using the datetime() constructor with parameters for year, month, and day.

# Example: Creating a date object
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

# The strftime() Method
# The strftime() method formats date objects into readable strings.

# Example: Displaying the name of the month
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))
