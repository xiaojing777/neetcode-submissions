class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = [1]*len(nums)
        right_prod = [1]*len(nums)
        left_prod[1] = nums[0]
        right_prod[len(nums)-2] = nums[-1]

        result = [0]*len(nums)

        for i in range(2, len(nums)):
            left_prod[i] = left_prod[i-1]*nums[i-1]
        
        for i in range(len(nums)-3, -1, -1):
            right_prod[i] = right_prod[i+1]*nums[i+1]

        for i in range(len(nums)):
            result[i] = (left_prod[i])*(right_prod[i])

        return result

        