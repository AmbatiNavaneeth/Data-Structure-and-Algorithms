>>>Max average subarray I
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:   #brut force approach
        max_avg=float('-inf')
        for i in range(len(nums)-k+1):
            summ=sum(nums[i:i+k])
            avg=summ/k
            max_avg=max(avg,max_avg)
        return max_avg
