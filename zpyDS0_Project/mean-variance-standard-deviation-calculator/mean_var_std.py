# https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float
import numpy as np


def calculate(list):
    axis_lookup = [0, 1, None]
    # if (not all(ele.isnumeric() for ele in list)):
    #     return TypeError
    try:
        arr_np = np.array(list).reshape(3, 3)
    except:
        raise ValueError("List must contain nine numbers.")
    else:
        return {
            "mean": [
                np.mean(arr_np, axis=axis_ref).tolist() for axis_ref in axis_lookup
            ],
            "variance": [
                np.var(arr_np, axis=axis_ref).tolist() for axis_ref in axis_lookup
            ],
            "standard deviation": [
                np.std(arr_np, axis=axis_ref).tolist() for axis_ref in axis_lookup
            ],
            "max": [
                np.amax(arr_np, axis=axis_ref).tolist() for axis_ref in axis_lookup
            ],
            "min": [
                np.amin(arr_np, axis=axis_ref).tolist() for axis_ref in axis_lookup
            ],
            "sum": [np.sum(arr_np, axis=axis_ref).tolist() for axis_ref in axis_lookup],
        }
