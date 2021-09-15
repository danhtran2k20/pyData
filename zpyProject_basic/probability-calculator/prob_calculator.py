# https://stackoverflow.com/questions/3496518/using-a-dictionary-to-count-the-items-in-a-list/9604768#9604768
# https://stackoverflow.com/questions/44883905/randomly-remove-x-elements-from-a-list
import copy
from math import exp
import random

# Consider using the modules imported above.


class Hat:
    def __init__(self, **hats):
        self.contents = []
        for key, value in hats.items():
            for _ in range(value):
                self.contents.append(key)

    def draw(self, numDraw):
        if numDraw > len(self.contents):
            return self.contents
        else:
            to_delete = random.sample(range(len(self.contents)), numDraw)
            hat_draw = [self.contents[i] for i in to_delete]
            self.contents = [
                x for i, x in enumerate(self.contents) if not (i in to_delete)
            ]
            return hat_draw


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count_pass = 0
    # hat_reset = [ball for ball in hat.contents]
    hat_reset = copy.deepcopy(hat)
    for _ in range(num_experiments):
        ball_count = count_ball_draw(hat.draw(num_balls_drawn))
        # print('compare(ball_count, expected_balls):', compare(ball_count, expected_balls))
        if compare(ball_count, expected_balls):
            count_pass += 1
        hat = copy.deepcopy(hat_reset)
    return count_pass / num_experiments


def compare(ball_draw, expected_balls):
    # print('ball_draw, expected_balls:', ball_draw, expected_balls)
    compare_result = True
    for (key, value) in expected_balls.items():
        if ball_draw.get(key, -1) < value:
            compare_result = False
    return compare_result


def count_ball_draw(items):
    counts = dict()
    for i in items:
        counts[i] = counts.get(i, 0) + 1
    return counts


random.seed(95)
hat = Hat(blue=3,red=2,green=6)

probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
print('probability:', probability)
