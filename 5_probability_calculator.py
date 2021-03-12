import copy
import random
# Consider using the modules imported above.

class Hat:
  #Initializing the class hat with a variable number of arguments
  def __init__(self,**key_args):
    self.contents=[]
    for key,values in key_args.items():
      for value in range(values):
        self.contents.append(key)

  #Method that accept an argument showing the number of balls to draw from a hat
  def draw(self,balls):
    drawn_balls = []

    if balls >= len(self.contents):
      return self.contents

    # Picking a random ball from the bag without replacement
    for ball in range(balls):
      picked_ball = random.choice(self.contents)
      drawn_balls.append(picked_ball)
      self.contents.pop(self.contents.index(picked_ball))  
    
    return drawn_balls



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  desired_results=0

  for experiments in range(num_experiments):
    hat_copy = copy.deepcopy(hat)

    actual_hat = hat_copy.draw(num_balls_drawn)

    #Adding actual results to a dictionary
    actual_dict={ball:actual_hat.count(ball) for ball in set(actual_hat)}

    #Comparison between drawn balls and desired result:
    filters = True
    for key, value in expected_balls.items():
      if key not in actual_dict or actual_dict[key] < expected_balls[key]:
        filters = False
        break

    if filters:
      desired_results += 1

  probability = desired_results/num_experiments
  return probability
