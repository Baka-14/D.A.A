 int max_time=INT_MIN;
    cout<<max_time;
    for(int i=0;i<n;i++){ 
        if(jobs[i].profit>max_time){ 
            max_time=jobs[i].profit;
        }
    }

    int c=0;
    sort(jobs,jobs+n,comparision);
    int total=0;
    while(c<max_time){ 
        cout<<jobs[c].id<<" ";
        total+=jobs[c].profit;
        c++;
    }
    cout<<"total profit: "<<total;