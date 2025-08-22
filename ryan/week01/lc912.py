class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # return sorted(nums) # this works lol

        # merge sort
        # divide the list into half
        # sort each half
        # merge two sorted list
        # base case: len(l) == 1 or 2

        if len(nums) == 1:
            return nums
        if len(nums) == 2:
            return nums if nums[0] <= nums[1] else nums[::-1]
        
        # len >= 3
        # divide
        mid = len(nums) // 2

        # conquer
        l_sorted = self.sortArray(nums[:mid])
        r_sorted = self.sortArray(nums[mid:])

        # merge
        return self.merge(l_sorted, r_sorted)
        
    def merge(self, l1: List[int], l2: List[int])-> List[int]:
        # 2 pts method
        # init
        pt1, pt2 = 0, 0

        # handle small cases
        if len(l1) == 0:
            return l2
        if len(l2) == 0:
            return l1
        
        res = [] # merged list
        # both non empty
        while pt1 < len(l1) or pt2 < len(l2):
            if pt1 == len(l1):
                # l1 exhausted
                res.extend(l2[pt2:])
                break
            if pt2 == len(l2):
                # l2 exhausted
                res.extend(l1[pt1:])
                break
            # l1, l2 compare
            if l1[pt1] < l2[pt2]:
                res.append(l1[pt1])
                pt1 += 1
            else:
                res.append(l2[pt2])
                pt2 += 1
        return res
