>>>Max average subarray I
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:   #brut force approach
        max_avg=float('-inf')
        for i in range(len(nums)-k+1):
            summ=sum(nums[i:i+k])
            avg=summ/k
            max_avg=max(avg,max_avg)
        return max_avg
        
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:  #Optimal
        win_sum=sum(nums[:k])
        max_sum=win_sum
        for i in range(k,len(nums)):
            win_sum+=nums[i]-nums[i-k]
            max_sum=max(max_sum,win_sum)
        return max_sum/k

>>>Minimum Positive Sum Subarray 
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int: #Brut
        n=len(nums)
        valid=[]
        valid_sum=float('+inf')
        for i in range(n):
            for j in range(i+1,n+1):
                subarray=nums[i:j]
                if len(subarray)>=l and len(subarray)<=r:
                    valid.append(subarray)

        min_sum=float('+inf')  
        for j in range(len(valid)):
            summ=sum(valid[j])
            if summ>0:
                min_sum=min(summ,min_sum)
            else:
                continue
        return min_sum if min_sum!=float('+inf') else -1 

>>>Longest subarray with sum K

class Solution:
    def longestSubarray(self, nums, k):   #brutforce
        n=len(nums)
        valid=[]
        for i in range(n):
            for j in range(i+1,n+1):
                subarrays=nums[i:j]
                valid.append(subarrays)
        max_len=0
        for num in range(len(valid)):
            summ=sum(valid[num])
            if summ==k:
                max_len=max(max_len,len(valid[num]))
        return (max_len)
                    
                    

                

            
            








