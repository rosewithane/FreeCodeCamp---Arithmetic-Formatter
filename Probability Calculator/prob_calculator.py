import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for color, count in kwargs.items():
      self.contents.extend([color]*count)

  def draw(self, number_of_balls):
    if number_of_balls > len(self.contents):
      return self.contents
    drawn_balls = random.sample(self.contents, number_of_balls)
    for ball in drawn_balls:
      self.contents.remove(ball)
    return drawn_balls

  
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0
  for _ in range(num_experiments):
    new_hat = copy.deepcopy(hat)
    list = new_hat.draw(num_balls_drawn)  
    success = True
    for color, count in expected_balls.items():
      if list.count(color) < count:
        success = False
        break
      
    if success:
      M += 1
  return M / num_experiments
        
          
          
      
    
  
  
