def search(data, searching_item):
    for value in data:
        if value == searching_item:
            break
    else:
        return -1
    return 1

my_list = ['Kunal', 'rawat', 'ifbvh']
print(f"is Kunal Present in my_list: {search(my_list, 'Kunal')}")
print(f"is Kunalid Present in my_list: {search(my_list, 'Kunalid')}")