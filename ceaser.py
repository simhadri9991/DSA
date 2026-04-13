'''encrypt a word using ceaser cipher'''

word=input("Enter a word:")
key=int(input("Enter a key:"))
result=" "
for ch in word:
    if ch.isalpha():
        if ch.islower():
            new=chr(ord(ch)+key)
            result += new
        else:
            new=chr(ord(ch)+key)
            result += new
print(result)