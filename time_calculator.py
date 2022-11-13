def add_time(t, duration, day=None):
    '''
    freeCodeCamp: https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator
    :param t: current time given as '12:34 PM'
    :param duration: duration in hours and minutes as '12:23'
    :param day: (Optional) day of the week
    :return: an end time and day of week if it was supplied, and (n days later) info if >1 day later
    '''
    ## TIME ##
    am = False
    if t[-2:] == 'AM':
        am = True

    t_hours = t.split(':')[0]
    t_minutes = t.split(':')[1][:2]
    d_hours = duration.split(':')[0]
    d_minutes = duration.split(':')[1]
    hrs = (int(t_hours) + int(d_hours)) % 12                    # find hours (before looking at mins)
    hrs_div = (int(t_hours) + int(d_hours)) // 12               # find AM or PM, how many 12's fit into total hours
    mins = int(t_minutes) + int(d_minutes)                      # mins sum min 0 - max 118
    # mins_div = (int(t_minutes) + int(d_minutes)) // 60         # not necessary

    ampm = ''
    # if hrs_div % 2 == 0 and am or hrs_div % 2 != 0 and am is False: # even 12s means no change in AM/PM
    #     ampm = 'AM'
    # elif hrs_div % 2 == 0 and am is False or hrs_div % 2 != 0 and am: # odd 12s means AM and PM change
    #     ampm = 'PM'

    if hrs_div != 0:
        if am:
            ampm = 'PM'
        else:
            ampm = 'PM'
    elif hrs_div == 0:
        if am:
            ampm = 'AM'
        else:
            ampm = 'PM'

    if mins >= 60:
        hrs += 1
        mins = mins % 60
        if mins < 10:
            mins = f'0{mins}'

    ## DAY ##
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    days_gone = (int(t_hours) + int(d_hours)) // 24
    if day:
        day = day.lower().capitalize()
        idx = days.index(day)
        end_day = days[idx + days_gone % 7]
        print(day, end_day)

    ## OUTPUT ##
    if days_gone > 1:
        return f'{hrs}:{mins} {ampm} ({days_gone+1} days later)' + ' hello'
    elif days_gone > 1 and day in days:
        return f'{hrs}:{mins} {ampm}, {end_day} ({days_gone+1} days later)' + ' HELLO'
    elif day in days and days_gone < 1:
        return f'{hrs}:{mins} {ampm}, {end_day}' + ' BYE'
    return f'{hrs}:{mins} {ampm}' + ' yes'

print(add_time('11:43 PM', '24:20', 'tueSday'), '\n') # Should return: 12:03 AM, Thursday (2 days later)
print(add_time('11:43 AM', '0:20'),'\n') # Should return: 12:03 PM
print(add_time('11:30 AM', '2:32', 'Monday'),'\n') # Should return: 2:02 PM, Monday