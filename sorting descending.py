''' Descending order using sorting '''
n= int(input('enter num:'))
a=[]
for i in range(n):
    ele=int(input('enter element:'))
    a.append(ele)
print('unsorted arr:',a)
for i in range(n):
    for j in range(i,n-1):
        if a[i]<a[j+1]:
            a[i],a[j+1]=a[j+1],a[i]
print('sorted arr:',a)