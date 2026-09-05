# n=int(input("n: "))
# for i in range(1,n+1):
#     print(i**2)

n=int(input("n: "))   
for i in range(1,n+1):
    if i%2==0:
        print(f'{i} is even number')

n=int(input("n: "))   
for i in range(2,n+1,2):
    print(i)
    