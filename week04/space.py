x=1
n = int(input("Input a number : "))
for i in range(1,n+1):
    x = x * i
print(f"{n}! = {x}")
# 0(n) Time complexity
# 0(1) Space complexity