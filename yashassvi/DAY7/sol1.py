l=[]
n=int(input("Enter the elements of the list\n"))
for i in range(n):
    e = int(input())
    l.append(e)
l.sort()
print("Maximum number: " ,l[-1])
