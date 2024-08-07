import sys
from point import Point, point_location

def main():
  if len(sys.argv) != 3:
    print("Usage: " + sys.argv[0] + " x y")
    return 1

  try:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
  except ValueError:
    print("Must have an integer for x and y")
    return 1

  point = Point(x, y)
  point_location(point)

if __name__ == "__main__":
  sys.exit(main())
  
