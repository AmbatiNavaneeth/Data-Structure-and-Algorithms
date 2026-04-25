nums=[2,4,2,7,5,4,2,4]
f=float('-inf')
s=float('-inf')
for n in nums:
    if n>f:
        s=f
        f=n
    elif n>s and n!=f:
        s=n
print(s)

nums=[2,4,2,7,5,4,2,4]
i=0
j=len(nums)-1
while i<j:
    nums[i],nums[j]=nums[j],nums[i]
    i+=1
    j-=1
print(nums)


nums=[1,2,3,4,4,9,5]
for i in range(1,len(nums)):
    if nums[i]<nums[i-1]:
        print("Not")
        break
else:
    print("Yes")

n=[1,2,6,7]
for num in n:
    if num+1 in n:
        pass
    else:
        print(num+1)
        break


nums=[1,2,3,4,5]
k=3
nums.reverse()
print(nums)
nums[:k]=reversed(nums[:k])
nums[k:]=reversed(nums[k:])
print(nums)

n=[1,2,3,1,5,4,2,2,3]
target=4
i=0
j=len(n)-1
ans=[]
while i<j:
    if n[i]+n[j]<target:
        i+=1
    elif n[i]+n[j]>target:
        j-=1
    else:
        ans.append([n[i],n[j]])
        i+=1
        j-=1
print(ans)

n="sdasdff"
c=0
for ch in n:
    c+=1
print(c)
 
Lower to Upper
s="asdfdKJHHasd"
ans=""
for ch in s:
    if 'a'<=ch<='z':
        ans+=chr(ord(ch)-32)
    else:
        ans+=ch
print(ans)

Upper to Lower
s="asdfdKJHHasd"
ans=""
for ch in s:
    if 'A'<=ch<='Z':
        ans+=chr(ord(ch)+32)
    else:
        ans+=ch
print(ans)


s="asdsasfdf"
freq={}
for ch in s:
    freq[ch]=freq.get(ch,0)+1
print(freq)

for key in freq:
    if freq[key]==1:
        print(key)
        break
else:
    print("Not")
    
ANAGRAm
s="nagaram"
t="anagram"
if len(s)!=len(t):
    print(False)
else:
    for ch in s:
        if ch not in t:
            print(False)
            break
        elif s.count(ch)!=t.count(ch):
            print(False)
            break
    else:
        print(True)
        
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    count = {}

    for ch in s1:
        count[ch] = count.get(ch, 0) + 1

    for ch in s2:
        if ch not in count or count[ch] == 0:
            return False
        count[ch] -= 1
    return True
            
        
s="hello world n"
words=s.split()
print(words)
i=0
j=len(words)-1
while i<j:
    words[i],words[j]=words[j],words[i]
    i+=1
    j-=1
print(words)
print(" ".join(words))

n=10
a,b=0,1
for i in range(1,n):
    print(a,end=" ")
    a,b=b,a+b

nums=[3,2,3,1,3,6,8]
k=3
nums.sort()
print(nums[-k])

import heapq
arr=[3,4,2,1,6] 
k=3
print(heapq.nlargest(k, arr)[-1])

nums=[1,2,3,5,2,2,8,5,4]
freq={}
for num in nums:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
print(freq)

for i in freq:
    if freq[i]>1:
        print(i,end=' ')
    else:
        pass

dup=[]
seen=[]
for num in nums:
    if num in seen:
        dup.append(num)
    else:
        seen.append(num)
print(dup)


nums=[3,4,0,3,0,7,0]
i=0
for j in range(len(nums)):
    if nums[j]==0:
        nums[i],nums[j]=nums[j],nums[i]
        i+=1
print(nums)

MAJORITY ELEMENT
nums=[4,3,6,2,2,2,2]
freq={}
for num in nums:
    freq[num]=freq.get(num,0)+1
for i in freq:
    if freq[i]>len(nums)//2:
        print(i)

nums = [4,3,6,2,2]
candidate = None
count = 0
for num in nums:
    if count == 0:
        candidate = num
    count += (1 if num == candidate else -1)
if nums.count(candidate) > len(nums)//2:
    print(candidate)
else:
    print("No majority element")

LEAP YEAR
n=2024
if (n%400==0) or (n%4==0 and n%100!=0):
    print("Leap")
else:
    print("Not")
    

n=10
for i in range(1,n+1):
    print(i,end=' ')

PRINTING 1-N USING RECURSION
def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n,end=" ")
print_numbers(5)

FACTORIAL
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))

FIBANOCCI
def fibanocci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibanocci(n-1)+fibanocci(n-2)
print(fibanocci(5))

SUM OF DIGITS
def son(n):
    if n==0:
        return 0
    return n%10+son(n//10)
print(son(2323))

REVERSE A STRING
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]
