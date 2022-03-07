import copy

class Point:
  """Represents a point in 2-D space."""

class Rectangle():
  """Represents a rectangle.
    attributes: width, height, corner.
  """

def print_point(p):
  print('%g, %g' % (p.x, p.y))

def distance_between_point(x, y):
  if x > y:
    return x-y
  else:
    return y-x

def find_center(rect):
  p = Point()
  p.x = rect.corner.x + rect.width/2
  p.y = rect.corner.y + rect.height/2
  return p

def grow_rectangle(rect, width, height):
  rect.width += width
  rect.height += height

def move_rectangle(rect, dx, dy):
  rect.corner.x += dx
  rect.corner.y += dy

def new_move_rectangle(rect, dx, dy):
  box2 = copy.deepcopy(rect)
  box2.corner.x += dx
  box2.corner.y += dy
  return box2

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0
grow_rectangle(box, 50.0, 50.0)
move_rectangle(box, 50.0, 50.0)
box2 = new_move_rectangle(box, 100.0, 100.0)

center = find_center(box)
center1 = find_center(box2)
# print_point(center)
# print_point(center1)
print(isinstance(box, Rectangle))
