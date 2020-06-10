from bisect import bisect
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left=0
        right=len(nums)-1
        mid=(left+right)//2
        # print self.binary_search(nums,left,right,target)
        return self.binary_search(nums,left,right,target,mid)




    def binary_search(self, nums, left, right, target, mid):
    	mid=mid
    	# flag=890
    	if right >= left:
    		mid=int((left+right)/2)
    		if target == nums[mid]:
    			# print mid
    			return mid

    		elif target > nums[mid]:
    			left=mid+1
    			return self.binary_search(nums,left,right,target, mid)
    		elif target < nums[mid]:
    			right=mid-1
    			return self.binary_search(nums,left,right,target, mid)
    	else:
            return bisect(nums,target)