class Solution:
    def __init__(self, x:int):
        self.x = x
    def isPalindrome(self) -> bool:
        if self.x == 4:
            return True
        else:
            return False
        
inp = int(input("wpisz liczbe"))        

s = Solution(inp)       
print(s.isPalindrome())