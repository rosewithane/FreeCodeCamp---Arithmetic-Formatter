class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, new_width):
    self.width = new_width

  def set_height(self, new_height):
    self.height = new_height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * (self.width + self.height)

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** 0.5

  def get_picture(self):
    s = ""
    if self.width > 50 or self.height > 50:
      s = "Too big for picture."
    else:
      for _ in range(self.height):
        s += "*" * self.width + "\n"
    return s

  def get_amount_inside(self, shape):
    return self.get_area() // shape.get_area()

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)

  def set_side(self, side):
        self.width = side
        self.height = side

  def __str__(self):
      return f"Square(side={self.width})"
    
