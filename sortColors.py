class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        dict_out={}
        for i  in range(len(nums)):
        	dict_out[nums[i]]=nums.count(nums[i])

        print dict_out

        # nums=[]
        flag_count_len=0
        len_flag=0

        for j in dict_out:
        	flag_num_len=0
        	while(flag_num_len<dict_out[j]):
        		nums[len_flag]=j
        		flag_num_len=flag_num_len+1
        		len_flag=len_flag+1
        		
        	

        return nums





obj=Solution()
nums=[2,0,2,1,1,0]
print obj.sortColors(nums)
