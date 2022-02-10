# Gearing Up for Destruction
# ==========================

# As Commander Lambda's personal assistant, you've been assigned the task of configuring the LAMBCHOP doomsday device's axial orientation gears. It should be pretty simple -- just add gears to create the appropriate rotation ratio. But the problem is, due to the layout of the LAMBCHOP and the complicated system of beams and pipes supporting it, the pegs that will support the gears are fixed in place.

# The LAMBCHOP's engineers have given you lists identifying the placement of groups of pegs along various support beams. You need to place a gear on each peg (otherwise the gears will collide with unoccupied pegs). The engineers have plenty of gears in all different sizes stocked up, so you can choose gears of any size, from a radius of 1 on up. Your goal is to build a system where the last gear rotates at twice the rate (in revolutions per minute, or rpm) of the first gear, no matter the direction. Each gear (except the last) touches and turns the gear on the next peg to the right.

# Given a list of distinct positive integers named pegs representing the location of each peg along the support beam, write a function solution(pegs) which, if there is a solution, returns a list of two positive integers a and b representing the numerator and denominator of the first gear's radius in its simplest form in order to achieve the goal above, such that radius = a/b. The ratio a/b should be greater than or equal to 1. Not all support configurations will necessarily be capable of creating the proper rotation ratio, so if the task is impossible, the function solution(pegs) should return the list [-1, -1].

# For example, if the pegs are placed at [4, 30, 50], then the first gear could have a radius of 12, the second gear could have a radius of 14, and the last one a radius of 6. Thus, the last gear would rotate twice as fast as the first one. In this case, pegs would be [4, 30, 50] and solution(pegs) should return [12, 1].

# The list pegs will be given sorted in ascending order and will contain at least 2 and no more than 20 distinct positive integers, all between 1 and 10000 inclusive.

# -- Python cases --
# Input:
# solution.solution([4, 30, 50])
# Output:
#     12,1

# Input:
# solution.solution([4, 17, 50])
# Output:
#     -1,-1
from unittest import main

# ===================================
import numpy as np
from fractions import Fraction
import sympy as simp

def solution(pegs):
    pegLen = len(pegs)
    arrGear = np.eye(pegLen)
    arrGear += np.roll(arrGear, 1)
    arrGear[0][0] = 1
    arrGear[pegLen - 1][0] = 1
    arrGear[pegLen - 1][pegLen - 1] = -2
    # print(arrGear)
    arrGear_det = Fraction(round(np.linalg.det(arrGear)))

    # ===================

    arrGear_ext = [(pegs[i + 1] - pegs[i]) for i in range(pegLen - 1)] + [0]
    # print(arrGear_ext)

    arrResult = []
    for i in range(pegLen):
        arrGear_ext_temp = np.copy(arrGear)
        arrGear_ext_temp[:, i] = arrGear_ext
        # Ở đây ẩu round luôn kết quả vì numpy là numeric float tính ra lẻ
        # Dựa vào tính chất của ma trận toàn bộ số nguyên thì det sẽ là số nguyên
        # -> Dùng sympy luôn cho nhanh, khỏi set công thức tay
        # Cũng có thể convert ma trận từ đầu chỉ bao gồm dạng Fraction
        arrResult.append(Fraction(round(np.linalg.det(arrGear_ext_temp))) / arrGear_det)

    print(arrResult)
    result = [arrResult[0].numerator, arrResult[0].denominator]
    # print('temp res: ',result)
    # for gearItem in arrResult:
    #     print("gearItem:", gearItem)
    #     if gearItem.numerator < 0 or gearItem.numerator < gearItem.denominator:
    #         print('invalid gear: ', gearItem)
    #         result = [-1, -1]
    #         break
    if any(
        (gearItem.numerator < 1 or gearItem.numerator < gearItem.denominator)
        for gearItem in arrResult
    ):
        print('invalid')
        result = [-1, -1]

    # Hiển nhiên numerator sẽ là số nguyên nên < 1 thì 0 và giá trị âm sẽ loại
    print(result)
    return result
    # return (
    #     [-1, -1]
    #     if any(
    #         (gearItem.numerator < 1 or gearItem.numerator < gearItem.denominator)
    #         for gearItem in arrResult
    #     )
    #     else [arrResult[0].numerator, arrResult[0].denominator]
    # )


solution([5754,5756])

# ==============================
# Autotest
# main(module='test_prob22_linear_algebra', exit=False)

# ==============================
# https://stackoverflow.com/questions/40465866/google-foobar-gearing-up-for-destruction
