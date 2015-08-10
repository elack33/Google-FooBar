"""
For example, when a guard picks up the medical file for Rabbit #1235,
she would first add those digits together to get 11, then add those together to get 2, her final sum."

Write a function answer(x), which when given a number x,
returns the final digit resulting from performing the above described repeated sum process on x.
"""


def answer(x):
    first = str(x)
    first_list = []
    for each in first:
            first_list.append(int(each))
    while len(first_list) > 1:
        sum_list = sum(first_list)
        first_list = []
        for each in str(sum_list):
            first_list.append(int(each))
    return first_list[0]

