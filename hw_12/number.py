num = int(input('Enter number: '))
result = []
while num > 0:
    result.append(str(num % 1000))
    num //= 1000
print(f"Your result: {'.'.join(result[::-1])}")