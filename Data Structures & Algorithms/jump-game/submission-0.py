class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = [False] * len(nums)
        print(reachable)
        reachable[len(nums)-1] = True
        for i in range (len(nums)-1, -1, -1):
            for j in range(i+1, i+nums[i]+1):
                if(j >= len(nums)): break
                if reachable[j] == True:
                    reachable[i] = True;
        return reachable[0]