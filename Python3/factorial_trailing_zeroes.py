class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        a = 5
        
        while a <= n:
	        ans += (n // a)
	        a *= 5
        
        return ans
