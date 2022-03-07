class Time:
  """Represents the time of day.
  attributes: hour, minute, second
  """

def print_time(time):
  print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

def is_after(t1, t2):
  return t1.hour > t2.hour

def add_time(t1, t2):
  done = Time()
  done.hour = t1.hour + t2.hour
  done.minute = t1.minute + t2.minute
  done.second = t1.second + t2.second
  if done.second >=60:
    done.second -= 60
    done.minute += 1
  if done.minute >= 60:
    done.minute -= 60
    done.hour += 1
  
  return done

def increment(time, seconds):
  time.second += seconds
  if time.second >=60:
    time.second -= 60
    time.minute += 1

  if time.minute >= 60:
    time.minute -= 60
    time.hour += 1

def increment1(time, seconds):
  time1 = Time()
  time1.second = time.second
  time1.minute = time.minute
  time1.hour = time.hour
  time1.second +=seconds
  if time1.second >=60:
    time1.second -= 60
    time1.minute += 1

  if time1.minute >= 60:
    time1.minute -= 60
    time1.hour += 1
  return time1

def time_to_int(time):
  minute = time.minute + (time.hour * 60)
  second = time.second + (minute*60)
  return second

def int_to_time(second):
  time = Time()
  minute, time.second = divmod(second, 60)
  time.hour, time.minute = divmod(minute, 60)
  return time

def new_add_time(t1, t2):
  seconds = time_to_int(t1) + time_to_int(t2)
  time = int_to_time(seconds)
  return time

def new_increment(time, seconds):
  time1 = Time()
  time1 = Time()
  time1.second = time.second
  time1.minute = time.minute
  time1.hour = time.hour
  time1.second +=seconds
  seconds1 = time_to_int(time1)
  return int_to_time(seconds1)


time = Time()
time.hour = 11
time.minute = 59
time.second = 45

time1 = Time()
time1.hour = 8
time1.minute = 12
time1.second = 12

# done = add_time(time, time1)
# increment(time, 55)
# time2 = increment1(time, 56)
# done = new_add_time(time, time1)
time2 = new_increment(time1, 56)
print_time(time2)