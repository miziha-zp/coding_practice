"""
原地快排 + 查看相邻元素是否相同 O(nlogn)
"""
# class Solution1(object):
#     def findRepeatNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         #原地快排
#         def quick_sort(nums, start, end):
#             if start >= end:
#                 return
#             mid = nums[start]
            
#             low, high = start, end
            
#             while low < high:
#                 while low<high and nums[high]>=mid:
#                     high -= 1
#                 nums[low], nums[high] = nums[high], nums[low]
#                 while low <high and nums[low]< mid:
#                     low += 1
#                 nums[low], nums[high] = nums[high], nums[low]
            
#             nums[low] = mid
            
#             quick_sort(nums, start, low-1)
#             quick_sort(nums, low+1, end)
  
#         quick_sort(nums,0,len(nums)-1)
            
#         repeat = []
#         if nums[0] == nums[1]:
#             repeat.append(nums[0])
#         repeat += [value for index,value in enumerate(nums) if nums[index-1] == nums[index] and index >= 1]
#         return repeat[0]

class Solution(object):
    '''
    哈希表，时间复杂度O(n), 空间O(n)
    '''
    def findRepeatNumber(self, nums):
        repeatDict = {}
        for num in nums:
            if num not in repeatDict:
                repeatDict[num] = 1
            else:
                return num