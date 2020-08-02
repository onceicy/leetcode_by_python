class Solution70:
    def climbStairs(self, n: int) -> int:
        a0, a1, a2 = 0, 0, 1
        for i in range(1,n+1):
            a0 = a1
            a1 = a2
            a2 = a0 + a1
        return a2