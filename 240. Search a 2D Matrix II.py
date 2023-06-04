class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        self.found = False
        self.i_bound = len(matrix)
        self.j_bound = len(matrix[0])
        self.iterated = 1000000001
        self.search(matrix, target, 0, 0)
        return self.found

    def search(self, matrix: list[list[int]], target: int, i: int, j: int):
        if self.found:
            return
        if i >= self.i_bound or i < 0:
            return
        if j >= self.j_bound or j < 0:
            return
        if matrix[i][j] == self.iterated:
            return
        if matrix[i][j] == target:
            matrix[i][j] = self.iterated
            self.found = True
            return
        if matrix[i][j] > target:
            matrix[i][j] = self.iterated
            self.search(matrix, target, i - 1, j)
            self.search(matrix, target, i, j - 1)
            return
        if matrix[i][j] < target:
            matrix[i][j] = self.iterated
            self.search(matrix, target, i, j + 1)
            self.search(matrix, target, i + 1, j)
            return

s = Solution()
print(s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 0))