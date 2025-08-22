class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # 这道题其实就是尽可能的保留下来最多的区间，先按照结束的位置排序就对了
        # 结束时间越早越优，经典区间调度
        intervals.sort(key=lambda x: x[1])

        keep = 0               # 能保留的不重叠区间数
        end = float('-inf')    # 上一个被选中的区间的结束时间
        for s, e in intervals:
            if s >= end:       # 与上一个选中的区间不重叠，则选择它
                keep += 1
                end = e

        return len(intervals) - keep

