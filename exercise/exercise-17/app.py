from typing import Tuple


class Time:
    def print_time(time):
        print("%.2d:%.2d:%.2d" % (time.hour, time.minute, time.second))

    def time_to_int(time):
        minute = time.minute + time.hour * 60
        seconds = time.second + minute * 60
        return seconds
    def int_to_time(seconds):
        time = Time()
        minute, time.second = divmod(seconds, 60)
        time.hour, time.minute = divmod(minute, 60)
        return time
    def increment(self, seconds):
        seconds +=self.time_to_int()
        return Time.int_to_time(seconds)
    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return Time.int_to_time(seconds)

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
    def __add__(self, other):
        # seconds = self.time_to_int() + other.time_to_int()
        # return Time.int_to_time(seconds)
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)
    def __radd__(self, other):
        return self.__add__(other)

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)
    def __add__(self, other):
        if isinstance(other, Point):
            px = self.x + other.x
            py = self.y + other.y
            p = Point(px, py)
            return p
        if isinstance(other, Tuple):
            px = self.x + other[0]
            py = self.y + other[1]
            p = Point(px, py)
            return p

time = Time()
time.hour = 14
time.minute = 45
time.second = 45
# Time.print_time(time)
# time.print_time()
end = time.increment(1337)
# end.print_time()
# print(end.is_after(time))
time1 = Time(15, 5, 2)
time2 = Time(3, 5, 3)
time3 = Time(5, 12, 44)
total = sum([time1, time2, time3])
print(total)
# print(1544 + time1)
# print(time1 + time2)
# print(time1)
# time1.print_time()

p = Point(70, 60)
p1 = Point(40, 70)
p2 = (40, 50)
# print(p + p2)
# print(p)
# print('%d, %d' % (p.x, p.y))