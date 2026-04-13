'''Program to reverse words in a string'''

words=input("Enter words:").split()
for word in words:
    print(word[::-1], end=" ")
    
#Example:-
'''
Enter words:apple banana orange
elppa ananab egnaro 
'''
