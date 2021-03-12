###From README 4

class Rectangle:
  #Initializing rectangle object
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return "Rectangle(width={}, height={})".format(self.width, self.height)

  def set_width(self, width):
    self.width = width
    return self.width
  
  def set_height(self, height):
        self.height = height
        return self.height

  #obtaining the shape's area
  def get_area(self):
    area = self.width * self.height
    return area

  #obtaining shape's perimeter
  def get_perimeter(self):
    perim = (self.width * 2) + (self.height * 2)
    return perim

  #Principal diagonal of the shape
  def get_diagonal(self):
    diag = (self.width ** 2 + self.height ** 2) ** .5
    return diag

  #Showing a string of * that represents the shape.
  def get_picture(self):
    #No bigger than 50
    if self.width > 50 or self.height > 50:
      return("Too big for picture.")
    else:
      return( ( ("*" * self.width)+ "\n" ) * self.height)

  #Fitting shape inside another
  def get_amount_inside(self, shape):
    areaGuest = shape.get_area()
    areaHome = self.get_area()
    i = 0
    while areaHome>=areaGuest:
      areaHome = areaHome-areaGuest
      i+=1
    return i
            

class Square(Rectangle):
  #Take Initializing from rectangle class
  def __init__(self, side):
    self.width = side
    self.height = side

  def __str__(self):
    return "Square(side={})".format(self.width)

  #Square width = height
  def set_side(self, side):
    self.width = side
    self.height = side
    return self.width, self.height
               
