from numpy import double 

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


item_list.sort(key=lambda x: (x.profit/x.weight), reverse=True) 


for i in range(n): 
    if item_list[i].weight<w:
        w=w-item_list[i].weight
        profit+=item_list[i].profit
    
    else:
        profit+=(item_list[i].profit/item_list[i].weight)*w
        break 

print(profit)



   








       