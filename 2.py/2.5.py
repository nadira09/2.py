my_list=[7,5,3,3,2]
while my_list:
    n=int(input())
    my_list.append(n)
    a=sorted(my_list)[::-1]
    print(a)
