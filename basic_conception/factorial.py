
'''
求数的阶乘
'''

def factorial(n):
    m = 1
    if n == 1 :
        return 1
    for i in range(1,n+1):
        m *= i 
    return m 

x = 10
print("%d 的阶乘是 %d" %(x,factorial(x))) 
        