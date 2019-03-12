"""
You are presented with an integer number larger than 5. Your goal is to identify the longest side
possible in a right triangle whose sides are not longer than the number you are given.

For example, if you are given the number 15, there are 3 possibilities to compose right triangles:

1. [3, 4, 5]
2. [6, 8, 10]
3. [5, 12, 13]

The following function shows one way to solve the problem but the code is not ideal or efficient.
Refactor the code based on what you have learned about code simplicity and efficiency.
"""


def maximum_right_triangle_side(max_side_value):
    solutions = []
    for hypotenuse in range(5, max_side_value):
        for side_1 in range(4, max_side_value):
            for side_2 in range(3, max_side_value):
                if hypotenuse * hypotenuse == side_1 * side_1 + side_2 * side_2:
                    solutions.append([hypotenuse, side_1, side_2])
    max_right_side = 0
    for solution in solutions:
        if max_right_side < max(solution):
            max_right_side = max(solution)
    return max_right_side


max_side = input("What is the maximal length of the triangle side? Enter a number: ")

print(f"The longest side possible is  {maximum_right_triangle_side(int(max_side))}")
