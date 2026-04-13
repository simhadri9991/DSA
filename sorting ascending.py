''' Ascending order using sorting '''
n= int(input('enter num:'))
a=[]
for i in range(n):
    ele=int(input('enter element:'))
    a.append(ele)
print('unsorted arr:',a)
for i in range(n):
    for j in range(0,n-i-1):
        if a[j]<a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print('sorted arr:',a)