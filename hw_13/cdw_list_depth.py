# https://www.codewars.com/kata/56b3b9c7a6df24cf8c00000e/train/python

def list_depth(list_array):
    if isinstance(list_array, list):
        depth = []
        for val in list_array:
            depth += list_depth(val),
        return 1 + (max(depth) if depth else 0)
    return 0
