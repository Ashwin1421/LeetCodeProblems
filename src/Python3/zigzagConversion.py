class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s:
            return ""
        elif numRows == 0 or numRows == 1:
            return s
        
        rows = [[] for _ in range(numRows)]
        down = False
        currentRow = 0
        for char in s:
            rows[currentRow].append(char)
            if currentRow == 0:
                down = True
            elif currentRow == (numRows-1):
                down = False
            if down:
                currentRow += 1
            elif not down:
                currentRow -= 1
        result = ""
        for r in rows:
            result += "".join(r)

        return result