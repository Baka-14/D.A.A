import matplotlib.pyplot as plt  
x=[5,10,15,20] 
y=[4.524999999944157e-05,8.72080000036135e-05,0.00010641699126780485,0.0002641699999780485]

fig = plt.figure(figsize = (10,5))
plt.plot(x,y, "or", color = "g")
plt.title("0-1 Knapsack")
plt.xlabel("Input size")
plt.ylabel("Time")
plt.show()
