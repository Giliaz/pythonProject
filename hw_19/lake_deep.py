# -------------------logical block----------------------
def lake_deep(deep: list) -> int:
    if not deep:
        return 0
    max_h = min_h = int(deep[0])
    result = []

    for h in deep:
        if h > max_h:
            result.append(max_h - min_h)
            max_h = min_h = h
        elif h < min_h:
            min_h = h
        else:
            result.append(h - min_h)

    visual_lake(deep)  # on/of visualization
    return max(result)


# ----------------visualization block--------------------
def visual_lake(deep: list) -> None:
    visual = [[deep[j] if i < deep[j] else ' ' * len(str(deep[j])) for j in range(len(deep))] for i in range(max(deep))]
    [print(*visual[i][:]) for i in range(max(deep) - 1, -1, -1)]
    print(*['~' * len(str(deep[i])) for i in range(len(deep))])
    return


assert (lake_deep([1, 2, 5, 6, 1, 2, 2, 3, 0, 1, 5, 6, 7, 5, 5, 7, 8, 8, 2]) == 6)
assert (lake_deep([8, 0, 5, 8, 7, 3, 8, 1, 10, 0, 7, 11, 11]) == 10)
assert (lake_deep([1, 6, 3, 9, 12, 18, 10, 12, 16]) == 6)
assert (lake_deep([9, 0, 7, 12, 2, 10, 0, 11]) == 11)
assert (lake_deep([10, 1, 9, 12, 5, 12]) == 9)
assert (lake_deep([1, 0, 3]) == 1)
assert (lake_deep([1]) == 0)
assert (lake_deep([]) == 0)