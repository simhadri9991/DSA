'''Program to find the smallest word lexcographically from the given list of words '''

words= input("Enter words:").split()
min_word=words[0]
for word in words:
    if word<min_word:
        min_word=word
print("Smallest words is:",min_word)

#Example:-
'''
Enter words:bad boy box        
Smallest words is: bad
'''