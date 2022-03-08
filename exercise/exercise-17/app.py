class Time:
    def print_time(time):
        print("%d:%d:%d" % (time.hour, time.minute, time.second))

    def time_to_int(time):
        minute = time.minute + time.hour * 60
        seconds = time.second + minute * 60
        return seconds


time = Time()
time.hour = 14
time.minute = 45
time.second = 45
# Time.print_time(time)
# time.print_time()
print(Time.time_to_int(time))
