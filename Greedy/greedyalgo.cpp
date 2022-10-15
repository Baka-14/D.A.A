#include<iostream>

using namespace std; 

struct job{ 
    char id;
    int deadl;//deadline
    int profit;//profit 
};

bool comparision(job a,job b){ 
    return (a.profit>b.profit);
}

int main(){ 
    cout<<"Please enter the no of jobs: ";
    int n;
    cin>>n;
    cout<<"Please enter the job id , job deadline,and the profit: ";
    job jobs[n];
    for( int i =0;i<n;i++){ 
        cin>>jobs[i].id;
        cin>>jobs[i].deadl;
        cin>>jobs[i].profit;
    }  
    
    int max_time=-99999;

    for(int i=0;i<n;i++){ 
        if(jobs[i].deadl>max_time){ 
            max_time=jobs[i].deadl;
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

}
