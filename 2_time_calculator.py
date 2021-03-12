def add_time(start, duration,day=None):
  # Splitting start time
  split_start = start.split()
  start_meridiem = split_start[1]
  split_start_time = split_start[0].split(':')
  start_hour = int(split_start_time[0])
  start_minute = int(split_start_time[1])
  #Splitting duration 
  split_duration = duration.split(':')
  d_hours = int(split_duration[0])
  d_mins = int(split_duration[1])

  # Calculate quantity in 12 hours format
  meridiems = int(d_hours) // 12
  # Calculate quantity of days later for the output. Later would be change
  days_later = meridiems // 2

  # Changing to 24 hours format , Calculates the new time
  time_minus_days = (start_hour + d_hours) - (24 * days_later)
  if start_meridiem == "PM":
    time_minus_days += 12
  if time_minus_days > 23:
    time_minus_days -= 24
    days_later += 1   
 
  # Calculate the new meridiem and hour
  if time_minus_days >= 12:
    end_hour = time_minus_days - 12
    end_meridiem = "PM"
  else:
    end_hour = time_minus_days
    end_meridiem = "AM"

  # Calculate the new minutes
  end_mins = start_minute + d_mins
  if end_mins > 59:
    end_hour += 1
    if end_meridiem == "AM" and end_hour == 12:
      end_meridiem = "PM"
    elif end_meridiem == "PM" and end_hour == 12:
      end_meridiem = "AM"
      days_later += 1
    end_mins -= 60

  # Finding out the new day
  if day != None:
  # Format day
    day = day.lower()
    day = day.capitalize()

    newday = ""  # This will be the new day in our output
    week_days = {"Monday" : 1, "Tuesday" : 2, "Wednesday" : 3, "Thursday" : 4, "Friday" : 5, "Saturday" : 6, "Sunday" : 7}
    if day in week_days:  # Verifying correct day
      day_value = week_days.get(day)
      days_ahead = day_value + days_later
      while days_ahead > 7:
        days_ahead -= 7
      for key, value in week_days.items():  #using dict of week_days to match days
        if days_ahead == value:
          newday = key

  # Build output string
  new_time = str(end_hour) + ":" + "{:02d}".format(end_mins) + " " + str(end_meridiem)
  if day != None:
    new_time = new_time + ", " + newday
  if days_later == 1:
    new_time = new_time + " (next day)"
  elif days_later >= 2:
    new_time = new_time + " (" + str(days_later) + " days later)"

  new_time.rstrip()

  return new_time
