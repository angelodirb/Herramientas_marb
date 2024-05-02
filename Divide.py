def divide(num1, num2):
    if num2 == 0:
        result = None
        print("You cannot divide by 0")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} is equal to {result}")
    return result
