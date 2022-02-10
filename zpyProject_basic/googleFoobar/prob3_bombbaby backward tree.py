# Bomb, Baby!
# ===========

# You're so close to destroying the LAMBCHOP doomsday device you can taste it! But in order to do so, you need to deploy special self-replicating bombs designed for you by the brightest scientists on Bunny Planet. There are two types: Mach bombs (M) and Facula bombs (F). The bombs, once released into the LAMBCHOP's inner workings, will automatically deploy to all the strategic points you've identified and destroy them at the same time.

# But there's a few catches. First, the bombs self-replicate via one of two distinct processes:
# Every Mach bomb retrieves a sync unit from a Facula bomb; for every Mach bomb, a Facula bomb is created;
# Every Facula bomb spontaneously creates a Mach bomb.

# For example, if you had 3 Mach bombs and 2 Facula bombs, they could either produce 3 Mach bombs and 5 Facula bombs, or 5 Mach bombs and 2 Facula bombs. The replication process can be changed each cycle.

# Second, you need to ensure that you have exactly the right number of Mach and Facula bombs to destroy the LAMBCHOP device. Too few, and the device might survive. Too many, and you might overload the mass capacitors and create a singularity at the heart of the space station - not good!

# And finally, you were only able to smuggle one of each type of bomb - one Mach, one Facula - aboard the ship when you arrived, so that's all you have to start with. (Thus it may be impossible to deploy the bombs to destroy the LAMBCHOP, but that's not going to stop you from trying!)

# You need to know how many replication cycles (generations) it will take to generate the correct amount of bombs to destroy the LAMBCHOP. Write a function solution(M, F) where M and F are the number of Mach and Facula bombs needed. Return the fewest number of generations (as a string) that need to pass before you'll have the exact number of bombs necessary to destroy the LAMBCHOP, or the string "impossible" if this can't be done! M   and F will be string representations of positive integers no larger than 10^50. For example, if M = "2" and F = "1", one generation would need to pass, so the solution would be "1". However, if M = "2" and F = "4", it would not be possible.

# -- Python cases --
# Input:
# solution.solution('4', '7')
# Output:
#     4

# Input:
# solution.solution('2', '1')
# Output:
#     1

# ==============================

# https://webcache.googleusercontent.com/search?q=cache:KfA4gr4HZrsJ:https://medium.com/%40chris.bell_/google-foobar-as-a-non-developer-level-3-64782678cbe0+&cd=6&hl=en&ct=clnk&gl=vn
# https://github.com/ivanseed/google-foobar-help/blob/master/challenges/bomb_baby/bomb_baby.md
# https://github.com/ivanseed/google-foobar-help
# https://surajshetiya.github.io/Google-foobar/
# https://blog.ishandeveloper.com/foobar-2020
# https://medium.com/@chris.bell_/google-foobar-as-a-non-developer-fc43e56af08f

# ==============================

# https://stackoverflow.com/questions/5292303/how-does-tuple-comparison-work-in-python#:~:text=Tuples%20are%20compared%20position%20by,the%20third%20and%20so%20on.

# x,y là số dạng str, py tự convert qua long nếu quá lớn
# x hoặc y = 1, vì cả x,y > 0 => k , 1 => cycle = k-1 + (cycle = 0)

def solution(x, y):
    x, y = int(x), int(y)
    cycles = 0
    while x != 1 and y != 1:
        x, y = max(x, y), min(x, y)
        # Bắt buộc swap trước vì 2%4 = 2
        if x % y == 0:
            return "impossible"
        else:
            cycles = cycles + int(x / y)
            x, y = y, x % y
    return str(cycles + max(x,y) - 1)


print(solution(2, 4))
print(solution(6, 3))
print(solution(7, 4))
print(solution(1, 5))
print(solution(7, 1))
