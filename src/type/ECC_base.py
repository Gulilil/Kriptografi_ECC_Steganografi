from type.point import Point

class ECCBase:

  def __init__ (self, a: int, b: int, p: int, basePoint: Point ):
    self.a = a
    self.b = b
    self.p = p
    self.basePoint = basePoint