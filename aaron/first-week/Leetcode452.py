class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # 按右端点排序（结束越早越优）
        points.sort(key=lambda x: x[1])

        arrows = 1                   # 至少需要一支箭
        end = points[0][1]           # 当前这支箭射在的水平位置（选第一个区间的右端）

        for s, e in points[1:]:
            if s <= end:
                # 与当前箭位置有交集，这个气球也会被同一支箭射爆
                continue
            # 无交集，需要新的一支箭，并把箭的位置更新为当前区间的右端
            arrows += 1
            end = e

        return arrows