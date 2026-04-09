# Date and Time Example 7
# This program demonstrates basic date and time operations.

from datetime import datetime, timedelta

# Current date and time
now = datetime.now()
print(f"Current date and time: {now}")

# Formatting date and time
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted date and time: {formatted_date}")

# Adding a timedelta
future_date = now + timedelta(days=7)
print(f"Date after 7 days: {future_date}")
