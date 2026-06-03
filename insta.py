✅n=145
temp=n
tot=0
while n>0:
    dig=n%10
    fact=1
    for i in range(1,dig+1):
        fact*=i
    tot+=fact
    n//=10
if tot==temp:
    print(True)
else:
    print(False)

✅
n=123000001
summ=0
while n>0:
    summ+=n%10
    n//=10
print(summ)

✅
n=12345
rev=0
while n>0:
    dig=n%10
    rev=rev*10+dig
    n//=10
print(rev)

✅lcm smallest number that divides both exactly
def lcm(a, b):
    greater = max(a, b)

    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1
print(lcm(12, 18))

✅
hcf largest number that divides both exactly
def hcf(a, b):
    while b:
        a, b = b, a % b
    return a

print(hcf(12, 18))

✅sum of two fractions
Python Program
n1 = 1
d1 = 2

n2 = 3
d2 = 4

num = n1 * d2 + n2 * d1
den = d1 * d2

print(f"{num}/{den}")

✅prime numbers in a range 
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

for num in range(1, 21):
    if is_prime(num):
        print(num, end=" ")


✅def is_arm(n):
    temp=n
    tot=0
    while n>0:
        dig=n%10
        tot+=dig**len(str(n))
        n//=10
    if temp==tot:
        return True
    else:
        return False
x=500
for i in range(1,x+1):
    if is_arm(i):
        print(i,end=" ")
second method
for num in range(1, 501):
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    if total == num:
        print(num, end=" ")
        
✅program to represent a number as sum of two prime numbers
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
num = 34
for i in range(2,(num//2)+1): num//2 to handle the duplicates
    if is_prime(i) and is_prime(num-i):
        print(f"{num}={i}+{num-i}")

✅write a program to find number of days in a given month of a given year
month=int(input())
year=int(input())

if month in [1,3,5,7,8,10,12]:
    print("31")

elif month in [4,6,9,11]:
    print("30")

elif month==2:
    if (year%400==0 )or (year%4==0 and year%100!=0):
        print("27")
    else:
        print("28")
else:
    print("invalid")

✅permutation of string
from itertools import permutations
s = "ABC"
for p in permutations(s):
    print("".join(p))

import math 
a=5
b=3
permutation =math.factorial(a)//math.factorial(a-b)
print(permutation)

✅to count 3 in range 
n = 35
count = 0
for i in range(n + 1):
    temp = i
    while temp > 0:
        if temp % 10 == 3:
            count += 1
        temp //= 10
print(count)

✅decimal to binary
n=13
ans=""
while n>0:
    dig=n%2
    ans=str(dig)+ans
    n//=2
print(ans)

✅# binary to decimal
binn="1101"
power=0
ans=0
for i in range(len(binn)-1,-1,-1):
    cal=(2**power)*int(binn[i])
    ans+=cal
    power+=1
  
print(ans)

✅array type sorted,unsorted or mixed
if array=sorted(array):
    print("Sorted")
elif array=sorted(array,reverse=True):
    print("unSorted")
else:
    print("mixed")

✅max and min
a=[1,7,4,9,3,2,0]
lar=float('-inf')
sma=float("inf")
for num in a:
    if num>lar:
        lar=num
    if num<sma:
        sma=num
print(lar)
print(sma)
