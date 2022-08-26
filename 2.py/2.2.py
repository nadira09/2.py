s=input()
S=list(s)
for el in range(0,len(s)-1,2):
    tmp=S[el]            
    S[el]=S[el+1]
    S[el+1]=tmp
print(S)