import copy
import random
# Consider using the modules imported above.

class Hat:
  myBalls = []
  contents = []

  def __init__(self, **balls):
    self.myBalls = balls
    for key in self.myBalls.keys():
      self.contents.append(key)

#def experiment(hat, expected_balls, num_balls_drawn, num_experiments):


#random.seed(95)
hat = Hat(blue=4, red=2, green=6)
print(hat.myBalls)
print(hat.contents)
#probability = experiment(
#    hat=hat,
#    expected_balls={"blue": 2,
#                    "red": 1},
#    num_balls_drawn=4,
#    num_experiments=3000)
#print("Probability:", probability)