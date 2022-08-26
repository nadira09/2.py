strg=input('Введите слова через пробел: ')

els=strg.split(' ')
cntr=1

for i in range(len(els)):
    print('\n',cntr,els[i][0:10],end='')
    cntr+=1
