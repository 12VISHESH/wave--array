l=[1,2,3,4,5]
j=len(l)-1
for i in range(j):
    if(i<=len(l)/2):
        print(l[i])
    if(j>len(l)/2):
        print(l[j])
    j-=1    