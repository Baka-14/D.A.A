import timeit
import matplotlib.pyplot as plt 

num=int(input("Please enter the size of the array:")) 
arr=[]
for i in range(0,num):
    l=int(input())
    arr.append(l)

a=int(input("Please enter the number to searched:"))

flag=0
starttime = timeit.default_timer()
for i in range(num):
     if arr[i]==a:
        print("Number found")
        flag=1

if flag==0:
    print("Number not found")
    

print("The time difference is :", timeit.default_timer() - starttime)

x=[5,10,15,20] 
y=[4.524999999944157e-05,5.2542000002375744e-05,9.53750000007858e-05,8.820799999753604e-05]

fig = plt.figure(figsize = (10,5))
plt.plot(x,y, "or", color = "b")
plt.title("Linear Search")
plt.xlabel("Input size")
plt.ylabel("Time")
plt.show()