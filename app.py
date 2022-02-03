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



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  ballsList = []
  for key in expected_balls.keys():
      while expected_balls[key] > 0:
        ballsList.append(key)
        expected_balls[key] -= 1
  print("The balls we're looking for are:", ballsList)
  
  drawnBalls = hat.draw(num_balls_drawn)
  print("Balls drawn from the hat were:", drawnBalls)

  successCount = 0
  for ball in ballsList:
    if ball in drawnBalls:
      print('Found the {foundBall} ball!'.format(foundBall=ball))
      drawnBalls.remove(ball)
      successCount += 1
  
  if successCount == len(ballsList):
    return "All balls matched!"
  else:
    return "Not a match."


#random.seed(95)
hat = Hat(blue=4, red=2, green=6)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
#print("Hat = ", hat.contents)
print("Probability:", probability)