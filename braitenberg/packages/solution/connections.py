from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    # these are random values
    res[:, :320] = 0
    res[300:, 100:320] = 0.1
    res[:, 320:] = 0
    res[300:, 320:540] = 0
    # ---
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    # these are random values
    res[:, 320:] = 0
    res[300:, 320:540] = 0.1
    res[:, :320] = 0
    res[300:, 100:320] = 0
    # ---
    return res
