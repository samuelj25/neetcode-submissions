class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m * n - 1

        while (l <= r):
            half = l + (r - l) // 2
            curr_row = half // n
            curr_col = half % n

            if (matrix[curr_row][curr_col] == target):
                return True
            elif (matrix[curr_row][curr_col] > target):
                r = half - 1
            else: # (matrix[curr_row][curr_col] < target)
                l = half + 1
        
        return False
