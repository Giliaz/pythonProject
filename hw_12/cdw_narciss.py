def cdw_narciss_num(number):
    num = number
    summ = 0
    while num > 0:
        summ += pow(num % 10, len(str(number)))
        num //= 10

    return number == summ


print(cdw_narciss_num(153))
print(cdw_narciss_num(1652))
