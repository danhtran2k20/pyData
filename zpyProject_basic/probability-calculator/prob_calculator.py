import copy
import random

# Consider using the modules imported above.


class Hat:
    def __init__(self, **hats):
        self.contents = []
        for key, value in hats.items():
            for _ in range(value):
                self.contents.append(key)
    def draw(self, numDraw):
        pass

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass


hat = Hat(blue=4, red=2, green=6)
print(hat.contents)
