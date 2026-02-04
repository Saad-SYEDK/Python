class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s) - 1
        newS = ""
        i , j = n, n

        while s[j] == " ":
            j -= 1

        i = j
        while i >= 0 and j > 0:
            if s[j] == " ":
                newj = self.skipSpaces(j, s)
                print(newj)
                newS += s[j+1 : i+1]
                newS += " "
                j = newj+1
                i = j-1
            j -= 1
        
        print (newS)
        newS += s[j+1 : i+1]
        return newS

    def skipSpaces(self, j ,s):
        while s[j] == " ":
            j -= 1
        return j

sol = Solution()
ans = sol.reverseWords("  hello world  ")

print(ans)