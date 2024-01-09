def replace_in_list(my_list, idx, element):
    for value in my_list:
        if value == my_list[idx]:
            my_list[my_list.index(value)] = element
        if value == my_list[-1]:
            break
    return my_list
