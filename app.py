import copy
import random
# Consider using the modules imported above.

class Hat:
  myBalls = []
  contents = []

  def __init__(self, **balls):
    self.myBalls = balls
    for key in self.myBalls.keys():
      while self.myBalls[key] > 0:
        self.contents.append(key)
        self.myBalls[key] -= 1
  
  def draw(self, numOfBalls):
    results = []
    if numOfBalls > len(self.contents):
      return  self.contents
    else:
      while numOfBalls > 0:
        pick = random.randint(0, len(self.contents) - 1)
        results.append(self.contents.pop(pick))
        numOfBalls -= 1
    return results



#def experiment(hat, expected_balls, num_balls_drawn, num_experiments):


#random.seed(95)
hat = Hat(blue=4, red=2, green=6)
print(hat.contents)
print(hat.draw(4))
#probability = experiment(
#    hat=hat,
#    expected_balls={"blue": 2,
#                    "red": 1},
#    num_balls_drawn=4,
#    num_experiments=3000)
#print("Probability:", probability)