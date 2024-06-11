from type.point import Point

class PairPoint:
  def __init__(self, p1: Point, p2: Point):
    self.p1 = p1
    self.p2 = p2

class PairPointValue:
  def __init__(self, p1: str, p2: str):
    self.p1Val = p1
    self.p2Val = p2