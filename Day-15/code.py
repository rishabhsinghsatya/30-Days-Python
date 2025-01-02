from datetime import datetime, timedelta, date

# 1. Current Date and Time
current_datetime = datetime.now()
print("Current Date and Time:", current_datetime)

# 2. Formatting Dates
formatted_date = current_datetime.strftime("%Y-%m-%d")
formatted_time = current_datetime.strftime("%H:%M:%S")
print("Formatted Date:", formatted_date)
print("Formatted Time:", formatted_time)

# 3. Parsing Dates from Strings
date_string = "2025-01-02"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
print("Parsed Date:", parsed_date)

# 4. Date Arithmetic
future_date = current_datetime + timedelta(days=7)
print("Date 7 Days from Now:", future_date)

past_date = current_datetime - timedelta(days=30)
print("Date 30 Days Ago:", past_date)

# 5. Difference Between Dates
date1 = date(2025, 1, 1)
date2 = date(2025, 1, 15)
difference = date2 - date1
print("Difference Between Dates:", difference.days, "days")

# 6. Getting Day of Week
day_of_week = current_datetime.strftime("%A")
print("Today is:", day_of_week)

# 7. Working with Time Only
time_only = current_datetime.time()
print("Current Time Only:", time_only)

# 8. Custom Date and Time
custom_datetime = datetime(2025, 12, 25, 10, 30, 0)
print("Custom Date and Time:", custom_datetime)
