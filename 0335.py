list = [6, 9, 5, 2, 6, 5, 6, 9]

new_list = []

def remove_duplicate(list):
    set_list = set(list)
    for i in set_list:
        new_list.append(i)
    
remove_duplicate(list)

print(new_list)