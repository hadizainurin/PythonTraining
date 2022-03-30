my_list = [-15, -26, 12, 1, 33, -24, 23, 76]
new_list = []
n = 4

while my_list:
    min = my_list[0]  
    for x in my_list: 
        if x < min:
            min = x
    new_list.append(min)
    my_list.remove(min)    

print(new_list)