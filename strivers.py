Max odd count 
nums="12354"  
c=0
max_len=0
for i in range(len(nums)):
    if int(nums[i])%2!= 0:
        c+=1
        max_len=max(max_len,c)
    else:
        c=0
print(max_len)

✅ Code for sum of digits:
def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total
