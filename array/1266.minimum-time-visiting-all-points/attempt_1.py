class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        sec = 0
        for i in range(n-1):
            point_start = points[i]
            point_end = points[i+1]
            sec += max(abs(point_start[0]-point_end[0]), abs(point_start[1]-point_end[1]))
        return sec
