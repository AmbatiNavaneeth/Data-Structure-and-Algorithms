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










