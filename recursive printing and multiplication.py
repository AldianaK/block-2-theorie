"""
Author: Aldiana Kucevic
Date: 23-12-2022
Function: Recursion Starting out with Python
"""


def count_down(num):
    """
    count down where it substracts 2 from a given number
    :param num:
    :return: -
    """

    if num == 0 or num == 1:  # Positive numbers
        return num
    else:
        print(num)
        count_down(num-2)  # -2 of every number

def recursive_multiplication(x, y):

    if x == 0:
        return x, y
    else:
        print(x*y)
        recursive_multiplication(x-1, y)
        # -1 because otherwise it would print 1 number a few times


def main():

    print("opdracht 1:")
    num = 12
    count_down(num)
    print("opdracht 2:")
    recursive_multiplication(6, 6)


main()