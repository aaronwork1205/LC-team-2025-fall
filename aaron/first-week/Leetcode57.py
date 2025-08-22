#
# @lc app=leetcode id=57 lang=python
#
# [57] Insert Interval
#

# @lc code=start
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []
        i, n = 0, len(intervals)
        newL, newR = newInterval  # 待插入区间的左右边界，后面会被扩展（合并）

        # 1) 把所有“完全在新区间左侧”的旧区间直接加入结果
        # 条件：当前区间的右端点 < newL，说明与新区间无重叠且在左边
        while i < n and intervals[i][1] < newL:
            res.append(intervals[i])
            i += 1

        # 2) 合并所有与新区间有重叠的区间
        # 重叠条件：当前区间的左端点 <= newR
        # 不断扩展 newL/newR，直到没有重叠为止

        # 这点跟for loop 不同的一点就是它能合并中间有交集的所有的interval
        while i < n and intervals[i][0] <= newR:
            newL = min(newL, intervals[i][0])  # 取更小的左界
            newR = max(newR, intervals[i][1])  # 取更大的右界
            i += 1
        res.append([newL, newR])  # 把合并后的大区间放入结果

        # 3) 把剩余“完全在右侧”的区间接到结果后面
        while i < n:
            res.append(intervals[i])
            i += 1

        return res
        

# @lc code=end