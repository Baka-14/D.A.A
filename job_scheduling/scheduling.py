import matplotlib.pyplot as plt  
import timeit

def job_scheduling(jobs, t):
    job_t = [(jobs[i],t[i]) for i in range(len(jobs))]
    job_t = sorted(job_t, key = lambda x : x[0], reverse=True)
    max_t = max(t)
    op_arr = [0 for i in range(max_t)]
    i = 0
    while i < max_t:
        if 0 not in op_arr:
            break
        j = 0
        while j < len(job_t): 
            curr_job, curr_dl = job_t[j]
            if op_arr[curr_dl-1] == 0:
                op_arr[curr_dl-1] = curr_job   
            else:
                k = curr_dl-1
                while k >= 0:
                    if op_arr[k] == 0:
                        op_arr[k] = curr_job
                        break
                    else:
                        k -= 1
            j += 1
        i += 1
    print()
    return op_arr

# jobs = [100,70,25,67]
# t = [2,1,2,1]
jobs = [35,10,70,38,28,80,23,16,25] 
t = [7,2,4,3,4,2,2,5,2]
print(jobs)
starttime = timeit.default_timer()
op = job_scheduling(jobs, t)
print("The sequence would be-:")
print(op, sum(op)) 
print("The time difference is :", timeit.default_timer() - starttime)

#ploting the graphs-:
x=[5,10,15,20] 
y=[3.524999999944157e-05,7.72080000036135e-05,0.00010641699126780485,0.0002641699999780485]

fig = plt.figure(figsize = (10,5))
plt.plot(x,y, "or", color = "black")
plt.title("Job Scheduling")
plt.xlabel("Input size")
plt.ylabel("Time")
plt.show()

