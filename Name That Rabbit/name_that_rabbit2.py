def answer(names):
    # your code here
    sorted_list = []
    big_list = []
    for each_name in names:
        num_list = []
        for each_char in each_name:
            num = ord(each_char) - 96
            num_list.append(num)
        sum_char = sum(num_list)
        big_list.append([sum_char] + num_list)
    big_list.sort(reverse=True)
    for blist in big_list:
        back_to_name = []
        for x in blist[1:]:
            back_to_char = chr(x + 96)
            back_to_name.append(back_to_char)
        sorted_list.append(''.join(back_to_name))
    return sorted_list

test = answer(["abc", "vi", "eeeeeea", 'fffffa', "al"])
print test
