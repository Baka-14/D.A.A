import timeit
import matplotlib.pyplot as plt  

def partition(array, low, high):
  pivot = array[high]
  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1

#quicksort function
def quickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    quickSort(array, low, pi - 1)
    quickSort(array, pi + 1, high)

#example question
data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)

size = len(data)
starttime = timeit.default_timer() 
quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data) 

print("The time difference is :", timeit.default_timer() - starttime)     

x=[5,10,15,20] 
y=[3.416599999994663e-05,4.754200000001152e-05,7.03750000000114e-05,8.399999999997299e-05]

fig = plt.figure(figsize = (10,5))
plt.plot(x,y, "or", color = "b")
plt.title("Quick Sort")
plt.xlabel("Input size")
plt.ylabel("Time")
plt.show()