def sum_list(numbers):
    return sum(numbers)

numbers = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]
result1 = sum_list(numbers)

def sum_digits(number):
    if number < 10:
        return number
    return (number % 10) + sum_digits(number // 10)

result2 = sum_digits(12345)

print(result1)
print(result2)  

