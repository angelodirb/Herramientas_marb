from add import add
from subtract import subtract
from Modulo import modulo
from Power import power
from multiply import multiply
from Divide import divide

def game():
    score = 0
    while True:
        print('======== Menu ========'
              '\n1. Add'
              '\n2. Subtract'
              '\n3. Multiply'
              '\n4. Divide'
              '\n5. Modulo'
              '\n6. Power'
              '\n0. Exit')
        option = int(input('\nChoose an option: '))
        if option == 0:
            break
        num_1 = int(input('Enter first number: '))
        num_2 = int(input('Enter second number: '))
        answer = int(input('Enter your answer: '))
        if option == 1:
            result = add(num_1, num_2)
            points = 1
        elif option == 2:
            result = subtract(num_1, num_2)
            points = 1
        elif option == 3:
            result = multiply(num_1, num_2)
            points = 2
        elif option == 4:
            result = divide(num_1, num_2)
            points = 2
        elif option == 5:
            result = modulo(num_1, num_2)
            points = 4
        elif option == 6:
            result = power(num_1, num_2)
            points = 4
        if result == answer:
            score += points
            print('Correct!!')
        else:
            print('Incorrect')
            break
    print(f'======== Game Over ========'
          f'\nYour score is {score}'
          '\nKeep going!')

game()
