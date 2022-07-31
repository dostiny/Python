def sum_of_repeat_nember(lis):
    total_num = 0
    for ex in ex_list:
        if ex_list.count(ex) == 1:
            total_num += ex
        
    return total_num

ex_list = [4, 4, 7, 8, 10, 4]
print(sum_of_repeat_nember(ex_list))