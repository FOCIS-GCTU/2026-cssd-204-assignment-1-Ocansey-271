# File:easter_date.py
# Description:Calculates the month and day of Easter Sunday using Gaus's computus algorithm.
# Assignment Number:3
#
# Name:Ocansey Elizabeth
# SID:2425401394
# Email:2425401394@live.gctu.edu.gh
# Grader: Buckman
# Sip days used this assignment:0
#
# On my honor,Ocansey Elizabeth, this programming assignment is my own work 
# and i have not provided this code to any other student.

# 1. Ask the user for the year and store it in a variable named 'year'
year_input = input("Enter year: ")
year = int(year_input)

# 2. Compute lunar year cycle position using the modulus operator
lunar_year_cycle_position = year % 19

# 3. Compute weekday slide parts using the modulus operator
weekday_slide_part_1 = year % 4
weekday_slide_part_2 = year % 7

# 4. Compute leap year factors using floor division
leap_year_100 = year // 100
leap_year_400 = leap_year_100 // 4

# 5. Calculate corrections and offsets using floor division and modulus
lunar_orbit_correction = (13 + 8 * leap_year_100) // 25
century_start = (15 - lunar_orbit_correction + leap_year_100 - leap_year_400) % 30
sunday_offset = (4 + leap_year_100 - leap_year_400) % 7

# 6. Calculate intermediate days added variables
days_added = (19 * lunar_year_cycle_position + century_start) % 30
day_of_week_offset = (2 * weekday_slide_part_1 + 4 * weekday_slide_part_2 + 6 * days_added + sunday_offset) % 7

# 7. Compute total days added
total_days_added = 22 + days_added + day_of_week_offset

# 8. Determine final day and month of Easter using floor division and modulus
day_of_easter = total_days_added % 31
month_of_easter = 3 + (total_days_added // 31)

# 9. Output the results matching the required format exactly
print("In " + str(year) + " Easter Sunday is on " + str(month_of_easter) + "/" + str(day_of_easter) + "/" + str(year) + ".")
