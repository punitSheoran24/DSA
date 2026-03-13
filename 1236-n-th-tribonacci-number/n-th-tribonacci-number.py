class Solution:
    def tribonacci(self, n: int) -> int:

        def fib(n,m):
            if n in m:
                return m[n]      
            else:
                m[n]=fib(n-3,m)+fib(n-2,m)+fib(n-1,m)
                return m[n]
        return fib(n,{0:0,1:1,2:1})
        