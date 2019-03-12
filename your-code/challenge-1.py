"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.
"""

print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')
a = input('Please choose your first number (zero to five): ')
b = input('What do you want to do? plus or minus: ')
c = input('Please choose your second number (zero to five): ')


def calculator(num1, command, num2):
    word_to_digit = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
    digit_to_word = {1: 'one', 2: 'two', 3: 'three', 4: 'four',
                     5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
                     0: 'zero', -1: 'negative one', -2: 'negative two', -3: 'negative three', -4: 'negative four',
                     -5: 'negative five'
                     }
    possible_commands = ['plus', 'minus']

    if num1 not in word_to_digit or num2 not in word_to_digit or command not in possible_commands:

        print("I am not able to answer this question. Check your input.")
    else:
        if command == 'plus':
            solution = word_to_digit[num1] + word_to_digit[num2]

        else:
            solution = word_to_digit[num1] - word_to_digit[num2]

        print(f'{num1} {command} {num2} equals {digit_to_word[solution]}')

    print("Thanks for using this calculator, goodbye :)")


calculator(a, b, c)
