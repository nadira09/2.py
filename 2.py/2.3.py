M=int(input('введите число от 1 до 12: '))
keys_m=[(1,2,12),(3,4,5),(6,7,8),(9,10,11)]
value_m=['winter','spring','summer','autumn']
dict_m=dict(zip(keys_m,value_m))
print(dict_m)
if M==1 or M==2 or M==12:
    print(dict_m.get((1,2,12)))
elif M==3 or M==4 or M==5:
    print(dict_m.get((3,4,5)))
elif M==6 or M==7 or M==8:
    print(dict_m.get((6,7,8)))
elif M==9 or M==10 or M==11:
    print(dict_m.get((9,10,11)))