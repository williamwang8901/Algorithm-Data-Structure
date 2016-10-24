import pdb
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k <= 0 or len(nums)  == 0:
            return
        length = len(nums)
        k %= length
        self.reverse(nums, 0, length - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, length - 1)

    def reverse(self, nums, start, end):
        pdb.set_trace()
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1

if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3]
    k = 1
    solution.rotate(nums, k)
