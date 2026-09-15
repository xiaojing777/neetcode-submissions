class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if nums[0]>0:
            return []

        result = []
        
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                i += 1
                continue
            l = i+1
            r = len(nums)-1
            while l<r:
                if l>i+1 and nums[l]==nums[l-1]:
                    l += 1
                    continue
                if r<len(nums)-1 and nums[r]==nums[r+1]:
                    r -= 1
                    continue
                if nums[i]+nums[l]+nums[r]==0:
                    result.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                elif nums[i]+nums[l]+nums[r]<0:
                    l+=1
                elif nums[i]+nums[l]+nums[r]>0:
                    r-=1

        return result

        