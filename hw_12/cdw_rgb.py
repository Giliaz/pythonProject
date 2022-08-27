def cdw_rgb(r, g, b):
    result = ''
    color = [r, g, b]
    for light in color:
        light = 0 if light < 0 else light
        light = 255 if light > 255 else light
        result += hex(light)[2:].upper() if len(hex(light)[2:]) == 2 else ('0' + hex(light)[2:])

    return(result)


print(cdw_rgb(257, 155, -2))