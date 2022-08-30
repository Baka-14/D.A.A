import matplotlib.pyplot as plt 
import time 

n=input().split()

def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)

y=[]
for i in n:
    s = time.time()
    (fib(int(i)))
    e=time.time()
    y.append((e-s))
    print(i)
print(y)

fig = plt.figure(figsize = (10,5))
plt.plot(n,y, "or", color = "b")
plt.title("Fibnaci sum series")
plt.xlabel("input size")
plt.ylabel("secs")
plt.show()



