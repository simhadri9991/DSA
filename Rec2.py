def funA(n):
    if n<=0:
        return
    print("A", n)
    funA(n-1)
def funB(n):
    if n<=0:
        return
    print("B", n)
    funA(n-1)
n=int(input("Enter a number:"))
funB(n)