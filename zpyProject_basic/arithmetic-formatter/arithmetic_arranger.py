def arithmetic_arranger(listProblems, calculate=False):
    line1, line2, dashLine, calculateLine = "", "", "", ""
    operatorAlign = "  "
    if len(listProblems) > 5:
        return "Error: Too many problems."

    for index, prob in enumerate(listProblems):
        [comp1, mathOperator, comp2] = prob.split(" ")
        # check input
        if mathOperator != "+" and mathOperator != "-":
           return "Error: Operator must be '+' or '-'."
        if len(comp1) > 4 or len(comp2) > 4:
            return "Error: Numbers cannot be more than four digits."
        if not comp1.isdecimal() or not comp2.isdecimal():
            return "Error: Numbers must only contain digits."
        # create template
        (compAlign1, compAlign2) = compAlign(comp1, comp2)
        probAlign = "" if index == 0 else "    "
        line1 += probAlign + operatorAlign + compAlign1 + comp1
        line2 += probAlign + mathOperator + " " + compAlign2 + comp2
        dashLen = 2 + max(len(comp1), len(comp2))
        dashLine += probAlign + dashLen * "-"
        calculateValue = str(eval(comp1 + mathOperator + comp2))
        if calculate:
            calculateLine += f"{probAlign}{calculateValue : >{dashLen}}"
    final = line1 + "\n" + line2 + "\n" + dashLine
    if calculate:
        final += "\n" + calculateLine
    # print(repr(final))
    return final


def compAlign(comp1, comp2):
    [compAlign1, compAlign2] = ["", ""]
    lenAlign = len(comp1) - len(comp2)
    if lenAlign > 0:
        compAlign2 = " " * lenAlign
    else:
        compAlign1 = " " * abs(lenAlign)
    return (compAlign1, compAlign2)
