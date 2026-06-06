class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        given an m x n matrix sorted in non-decreasing order, return
        true if the intger "target" exists in the matrix

        O(m * n) solution: just iterate through every element to try
        to find target

        binary search on row and column:
        
        left, right for rows:
        1. get middle, and then get start and end for that row to get a
        range of values.
        2. if target is in range, binary search that row. if target
        is less than range start, shift right to middle - 1. if target
        is greater than range start, shift left to middle + 1
        3. if we haven't found a valid row, return false
        4. once we're in the row, simple binary search through the row
        """
        m = len(matrix)
        n = len(matrix[0])

        left, right = 0, m - 1
        target_row = None

        while left <= right:
            middle = (left + right) // 2
            middle_start = matrix[middle][0]
            middle_end = matrix[middle][n - 1]

            if middle_start <= target and target <= middle_end:
                target_row = middle
                break
            elif target < middle_start:
                right = middle - 1
            elif target > middle_end:
                left = middle + 1

        if target_row == None:
            return False

        left, right = 0, n - 1
        while left <= right:
            middle = (left + right) // 2
            middle_num = matrix[target_row][middle]

            if middle_num == target:
                return True
            elif target < middle_num:
                right = middle - 1
            elif target > middle_num:
                left = middle + 1
        
        print("gurt")
        return False



