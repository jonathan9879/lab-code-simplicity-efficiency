"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.
"""


def random_string_generator(length=12,
                            letters=('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                                     'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4',
                                     '5', '6', '7', '8', '9')):
    counter = 0
    random_string = ''
    while counter < length:
        import random
        random_string += random.choice(letters)
        counter += 1
    return random_string


def batch_string_generator(number_of_strings, minimum_length=8, maximum_length=12):
    batch = []
    for i in range(number_of_strings):
        if minimum_length < maximum_length:
            import random
            string_length = random.choice(range(minimum_length, maximum_length))
        elif minimum_length == maximum_length:
            string_length = minimum_length
        else:
            import sys
            sys.exit('Incorrect min and max string lengths. Try again.')
        batch.append(random_string_generator(string_length))
    return batch


min_len = input('Enter minimum string length: ')
max_len = input('Enter maximum string length: ')
num_of_strings = input('How many random strings to generate? ')

print(batch_string_generator(int(num_of_strings), int(min_len), int(max_len)))
