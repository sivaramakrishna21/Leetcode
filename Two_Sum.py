class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output=[]
        val=nums[0]
        i=0
        while(1):
            val=nums[i]
            
            if target-val in nums[0:i]+nums[i+1::]:
                if(i==nums.index(target-val)):
                    return [i,(nums[0:i]+nums[i+1::]).index(target-val)+1]
                else:
                    return [i,nums.index(target-val)]
            else:
                i+=1
