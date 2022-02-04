import copy
import random
# Consider using the modules imported above.

class Hat:
  myBalls = []

  def __init__(self, contents=None, **balls):
    self.myBalls = balls
    if contents is None:
      contents = []
    self.contents = contents
    for key in self.myBalls.keys():
      while self.myBalls[key] > 0:
        self.contents.append(key)
        self.myBalls[key] -= 1
  
  def draw(self, numOfBalls):
    results = []
    workingContents = copy.copy(self.contents)
    if numOfBalls > len(workingContents):
      return  workingContents
    else:
      while numOfBalls > 0:
        pick = random.randint(0, len(workingContents) - 1)
        results.append(workingContents.pop(pick))
        numOfBalls -= 1
    return results



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  ballsList = []
  for key in expected_balls.keys():
      while expected_balls[key] > 0:
        ballsList.append(key)
        expected_balls[key] -= 1
  
  experimentCount = 0
  experimentMatches = 0
  while experimentCount < num_experiments:
    drawnBalls = hat.draw(num_balls_drawn)
    foundBalls = 0
    for ball in ballsList:
      if ball in drawnBalls:
        drawnBalls.remove(ball)
        foundBalls += 1

    if foundBalls == len(ballsList):
      experimentMatches += 1
      experimentCount += 1
    else:
      experimentCount += 1
  return (experimentMatches/experimentCount)



#random.seed(95)
hat = Hat(blue=4, red=2, green=6)
#print("Hat = ", hat.contents)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=1000)
print("Probability:", probability)