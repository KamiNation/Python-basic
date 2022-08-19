""" By providing 2 keywords that terminate a loop iteration prematurely. The py break statement immediately
    terminate a loop entirely. Program execution proceeds to the first statement follwoing the loop body
"""
x=0
n=10
while x<n:
    print(x)
    if x == 8:
        break
    x=x+1


n=5
while n>0:
    n -= 1
    if n==2:
        continue
    print(x)
