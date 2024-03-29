#!/usr/bin/python3
# -*- coding: utf-8 -*-

# =============================================================================
#
#        FILE:  main.py
#      AUTHOR:  Tan Duc Mai <henryfromvietnam@gmail.com>
#     CREATED:  2021-10-11
# DESCRIPTION:  Calculate how much a user will get paid after a day, week,
#               month, or year.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.
#
# =============================================================================

# Variable initialisation.
salary_per_hour = float(input('How much do you get paid per hour: '))

# Hour input validation.
hours_per_day = float(input('How many hours do you work per day: '))
while not 0 <= hours_per_day <= 24:
    print('ERROR: Invalid hour value')
    hours_per_day = float(input('How many hours do you work per day: '))

# Duration input validation.
duration = input('Enter the duration to calculate (day/week/month/year): ')
while duration not in ['day', 'week', 'month', 'year']:
    print('ERROR: Invalid duration')
    duration = input('Enter the duration to calculate (day/week/month/year): ')


# Now that we have a valid duration (day/week/month/year)
# calculate the salary based on the user input duration.

if duration == 'day':  # Calculate the salary earned per day.
    print(f'After a day you will earn ${salary_per_hour * hours_per_day}')

else:
    # Now that duration is either week/month/year
    # prompt the user for days spent working per week.
    days_per_week = int(input('How many days do you work per week: '))
    while days_per_week not in range(8):        # Day input validation.
        print('ERROR: Invalid day value')
        days_per_week = int(input('How many days do you work per week: '))

    # Initialisa a variable representing a common operation.
    long_term_salary = salary_per_hour * hours_per_day * days_per_week

    # Calculate the salary earned per week/month/year.
    if duration == 'week':
        print(f'After a {duration} you will earn ${long_term_salary}')

    elif duration == 'month':
        print(
            f'After a {duration} you will earn between ${long_term_salary*4}'
            f' and ${long_term_salary * 4.34524 : .2f}')

    else:
        print(
            f'After a {duration} you will earn between ${long_term_salary*48}'
            f' and ${long_term_salary * 52.1329 : .2f}')
