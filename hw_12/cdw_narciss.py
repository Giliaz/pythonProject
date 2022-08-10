def cdw_narciss_num(number):
    degree = len(str(number))
    num = number
    summ = 0
    while num > 0:
        summ += pow(num % 10, degree)
        num //= 10
    return number == summ


print(cdw_narciss(153))
print(cdw_narciss(1652))
