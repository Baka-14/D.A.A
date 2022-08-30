import matplotlib.pyplot as plt 
import time

n=[(2,4),(6,8),(5,10)]

def pow(n,p):
    if p==0:
        return 1
    else:
        return n*pow(n,p-1)

y=[]

for ele in n:
    s = time.time()
    pow(ele[0],ele[1])
    e = time.time()
    y.append((e-s))
    print(ele)
print(y)

fig = plt.figure(figsize = (10,5))
plt.plot(n,y, "or", color = "b")
plt.title("Power")
plt.xlabel("input size")
plt.ylabel("secs")
plt.show()




