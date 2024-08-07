
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

def point_location(point):
  match point:
    case Point(x=0, y=0):
      print("Origin")
    case Point(x=0, y=y):
      print(f"y={y}")
    case Point(x=x, y=0):
      print(f"x={x}")
    case Point(x=x, y=y):
      print(f"point x={x} and y={y}")
    case _:
      print("not a point")

