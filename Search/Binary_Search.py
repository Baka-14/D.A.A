import timeit
import matplotlib.pyplot as plt 

X=int(input("Enter the num to be searched: "))
num=int(input("Please enter the size of the array: ")) 
arr=[]
for i in range(0,num):
    l=int(input())
    arr.append(l) 

starttime = timeit.default_timer()
arr.sort()

def Binary_search(arr,start,end,x):
    if end>=start:
        mid=(start+end)//2
        
        if arr[mid]==x:
            return mid 
        
        elif arr[mid]>x:
            return Binary_search(arr,start,mid-1,x)
        
        else:
            return Binary_search(arr,mid+1,end,x) 
    else:
        return -1


foo=Binary_search(arr,0,num-1,X) 

if foo!=-1:
    print("Number Found") 

else:
    print("Number not Found")

print("The time difference is :", timeit.default_timer() - starttime)

x=[5,10,15,20] 
y=[4.524999999944157e-05,8.72080000036135e-05,0.00010641699999780485,9.370800000141344e-05]

fig = plt.figure(figsize = (10,5))
plt.plot(x,y, "or", color = "b")
plt.title("Binary Search")
plt.xlabel("Input size")
plt.ylabel("Time")
plt.show()
