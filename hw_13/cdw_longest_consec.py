# https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python

def longest_consec(strarr, k):
    result = ''
    if 0 < k <= len(strarr):
        for i in range(len(strarr)):
            line = ''
            if len(strarr) >= i + k:
                for j in range(k):
                    line += strarr[i + j]
                if len(line) > len(result):
                    result = line
            else:
                break
    return result
