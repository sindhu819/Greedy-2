'''
Leetcode- 135. Candy - https://leetcode.com/problems/candy/
time complexity - O(N)
space complexity - O(N)
Approach - first we assign each child one candy each
          2) Then we compare left neighbour, if it is greater then then we add 1 candy else it remains the same
          3) Sameway we do compare the right neighbour
          
          
'''
class Solution:
    def candy(self, nums: List[int]) -> int:
        m=len(nums)
        res=[1 for i in range(m)]
        
        #left neighbour
        for i in range(1,m,1):
            if nums[i]>nums[i-1]:
                res[i]=res[i-1]+1
        print(res)
        
        #right neighbour
        for i in range(m-2,-1,-1):
            if nums[i]>nums[i+1]:
                res[i]=max(res[i],res[i+1]+1)
        print(res)
        
        #calulate sum
        sum=0
        for i in range(len(res)):
            sum+=res[i]
        return sum
            