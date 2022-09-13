from heapq import merge
import timeit
import matplotlib.pyplot as plt  


def merge_sort(arr):
    if len(arr)>1:
        left_arr=arr[:len(arr)//2]
        right_arr=arr[(len(arr)//2):] 

        merge_sort(left_arr) 
        merge_sort(right_arr) 

        i=0
        j=0
        k=0 #used for merging 
        # print(left_arr)
        # print(right_arr)
        while i<len(left_arr) and j<len(right_arr): 
            if left_arr[i]<right_arr[j]:
                arr[k]=left_arr[i]
                i+=1 
            else:
                arr[k]=right_arr[j]
                j+=1 
            k+=1 
        while(i<len(left_arr)):
            arr[k]=left_arr[i]
            i+=1
            k+=1 

        while(j<len(right_arr)):
            arr[k]=right_arr[j] 
            j+=1
            k+=1 

arr=[2,6,5,1,7,4,6,7,1,2,8,35,3,5,9,10,25,31,69,55]

starttime = timeit.default_timer() 
merge_sort(arr)
print(arr)
print("The time difference is :", timeit.default_timer() - starttime)     

x=[5,10,15,20] 
y=[3.416599999994663e-05,4.754200000001152e-05,7.03750000000114e-05,8.399999999997299e-05]

fig = plt.figure(figsize = (10,5))
plt.plot(x,y, "or", color = "b")
plt.title("Merge sort")
plt.xlabel("Input size")
plt.ylabel("Time")
plt.show()
