def new_format(string):
    result = []
    while len(string) > 0:
        result.append(string[-3:])
        string = string[:-3]

    return '.'.join(result[::-1])


assert (new_format("1000000") == "1.000.000")
assert (new_format("100") == "100")
assert (new_format("1000") == "1.000")
assert (new_format("100000") == "100.000")
assert (new_format("10000") == "10.000")
assert (new_format("0") == "0")
