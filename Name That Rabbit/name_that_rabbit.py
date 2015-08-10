"""
You realize that if you assign the value 1 to the letter A, 2 to B, and so on up to 26 for Z,
and add up the values for all of the letters, the names with the highest total values will be
the professor's favorites. For example, the name Annie has value 1 + 14 + 14 + 9 + 5 = 43,
while the name Earz, though shorter, has value 5 + 1 + 18 + 26 = 50.

If two names have the same value, Professor Boolean prefers the lexicographically larger name.
For example, if the names were AL (value 13) and CJ (value 13), he prefers CJ.

Write a function answer(names) which takes a list of names and returns the list sorted in
descending order of how much the professor likes them.

There will be at least 1 and no more than 1000 names.
Each name will consist only of lower case letters. The length of each name will be at least 1 and no more than 8

Test cases
==========

Inputs:
    (string list) names = ["annie", "bonnie", "liz"]
Output:
    (string list) ["bonnie", "liz", "annie"]

Inputs:
    (string list) names = ["abcdefg", "vi"]
Output:
    (string list) ["vi", "abcdefg"]
"""

def answer(names):
    # your code here
    num_list = []
    sorted_list = []
    alpha = ['-', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
             't', 'u', 'v', 'w', 'x', 'y', 'z']
    while len(num_list) < len(names):
        for each_name in names:
            char_num = []
            for chars in each_name:
                char_num.append(alpha.index(chars))
            num_list.append(sum(char_num))

    new_list = sorted(num_list, reverse=True)

    for ind in new_list:
        if all(x == new_list[0] for x in new_list):
            sorted_list = sorted(names)
            print "All the same!"
        else:
            # need to sort values that are the same by alpha
            # i have a sorted list by sum, i need to sort by alpha on string
            print ind
            if (x == new_list[0] for x in new_list):
                print "some the same!  "
            val = num_list.index(ind)
            print val
            sorted_list.append(names[val])

    return sorted_list

test = answer(["vi", "eeeeeea", 'fffffa', "al"])
print test
