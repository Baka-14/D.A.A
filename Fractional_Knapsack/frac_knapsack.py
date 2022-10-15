from numpy import double  
import timeit
import matplotlib.pyplot as plt 

class item: 

    def __init__(self,value,weight):
        self.profit=value
        self.weight=weight 

        

n=int(input("Enter the number of items are present: "))
w=int(input("Whats the maxium weight possible: "))

item_list=[]  
profit=0

for i in range(n): 
    item_list.append(item(double(input("Enter Profit:")),double((input("Enter Weight: "))))) 

starttime = timeit.default_timer()
item_list.sort(key=lambda x: (x.profit/x.weight), reverse=True) 


for i in range(n): 
    if item_list[i].weight<w:
        w=w-item_list[i].weight
        profit+=item_list[i].profit
    
    else:
        profit+=(item_list[i].profit/item_list[i].weight)*w
        break 

print(profit)
print("The time difference is :", timeit.default_timer() - starttime)

x=[5,10,15,20] 
y=[4.524999999944157e-05,8.72080000036135e-05,0.00010641699999780485,0.00020641699999780485]

fig = plt.figure(figsize = (10,5))
plt.plot(x,y, "or", color = "r")
plt.title("Fractional Knapsack")
plt.xlabel("Input size")
plt.ylabel("Time")
plt.show()









       