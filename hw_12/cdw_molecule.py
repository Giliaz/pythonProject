def cdw_molecule(formula):
    # ______variable _____
    sub = []
    deep_sub = []
    temp = {}
    result = {}
    br_plus = br_multi = 0

    # _____start code_____
    sub.extend(formula)

    if '[' in sub:
        start = sub.index('[')
        end = sub.index(']') + 1
        br_plus += int(sub[end])
        deep_sub.append(sub[:start])
        sub = sub[start: end - 1]

    if '(' in sub:
        start = sub.index('(')
        end = sub.index(')') + 1
        br_multi += int(sub[end])
        deep_sub.append(sub[:start])
        sub = sub[start: end - 1]

    deep_sub.append(sub)

    flag = 0
    for inst in deep_sub:
        if '[' in inst:
            flag = 1
            start = inst.index('[')
            inst = inst[start + 1:]

        elif '(' in inst:
            flag = 2
            start = inst.index('(')
            inst = inst[start + 1:]

        for num in range(len(inst)):
            molecula = 1
            if inst[num].isupper():
                if num + 1 < len(inst) and inst[num + 1].islower():
                    temp[f'{inst[num]}{inst[num + 1]}'] = temp.get(f'{inst[num]}{inst[num + 1]}', 0) + molecula

                elif num + 1 < len(inst) and inst[num + 1].isdigit():
                    molecula = int(inst[num + 1])
                    temp[inst[num]] = temp.get(inst[num], 0) + molecula

                else:
                    temp[inst[num]] = temp.get(inst[num], 0) + molecula

        if flag == 1:
            for key, value in temp.items():
                temp[key] = value * br_plus

        if flag == 2:
            for key, value in temp.items():
                br_plus = br_plus if br_plus != 0 else 1
                temp[key] = value * br_multi * br_plus

        for key, value in temp.items():
            result[key] = result.get(key, 0) + value
        temp.clear()

    print(result)


cdw_molecule("H2O")  # ("H2O"), {'H': 2, 'O' : 1}, "Should parse water")
cdw_molecule("Mg(OH)2")  # ("Mg(OH)2"), {'Mg': 1, 'O' : 2, 'H': 2}, "Should parse magnesium hydroxide: Mg(OH)2")
cdw_molecule("K4[ON(SO3)2]2")  # {'K': 4,  'O': 14,  'N': 2,  'S': 4}, "Should parse Fremy's salt: K4[ON(SO3)2]2")
