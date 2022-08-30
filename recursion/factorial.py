import matplotlib.pyplot as plt 
import time

def fac(n):
    if n==1:
        return n
    else:
        return n*fac(n-1) 

x=[3*i for i  in range(1,10)]
y=[]

for ele in x:
    s = time.time()
    fac(ele)
    e = time.time()
    y.append((e-s))
    print(ele)
print(y)

fig = plt.figure(figsize = (10,5))
plt.plot(x,y, "or", color = "b")
plt.title("Factorial)")
plt.xlabel("input size")
plt.ylabel("secs")
plt.show()

