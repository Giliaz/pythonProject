def cdw_cakes(recipe, available):
    result = []
    for ingredients in recipe.keys():
        if ingredients in available.keys():
            result.append(available[ingredients] / recipe[ingredients])
        else:
            return 0

    return int(sorted(result)[0])


recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cdw_cakes(recipe, available))
