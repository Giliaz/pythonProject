# https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python

def sum_of_intervals(intervals):
    result = 0
    intervals.sort()
    start, stop = intervals[0]
    for x, y in intervals:
        if x <= stop:
            if y > stop:
                stop = y
        elif x > stop:
            result += abs(stop - start)
            start, stop = x, y
    result += abs(stop - start)
    return result