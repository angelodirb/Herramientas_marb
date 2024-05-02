def modulo(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot modulo by zero")
    result = num1 % num2
    print(f"{num1} % {num2} is equal to {result}")
    return result
