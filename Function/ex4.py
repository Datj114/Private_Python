import math
def inputed():
    """this function input x coordinate, y coordinate(toạ độ x, toạ độ y)"""
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    return x1, y1, x2, y2


def output(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


x1, y1, x2, y2 = inputed()
print(output(x1, y1, x2, y2))
