#include <iostream>
#include <vector>
#include <string>
using namespace std;


int binarySearch(vector<string> array, int l, int r, string x){
    if (l<=r){
        int mid = l + (r - l)/2;

        if (array[mid] == x)
            return mid;
        if (array[mid] > x)
            return binarySearch(array, l, mid-1, x);
        return binarySearch(array, mid+1, r, x);
    }
    return -1;
}

int main(){
    
    vector<string> array;

    string s;
    getline(cin , s);

    int q = 0;
    string t = "";
    while(q < s.size()){
        if(s[q] == ' '){
            array.push_back(t);
            t = "";
        }
        else{
            t += s[q];
        }
        q++;
    }
    array.push_back(t);

    bool flag = false;
    int i = 1;
    int x = i;
    while(!flag){
        if(array[0] == "$"){
            i = 0;
            flag = true;
            break;
        }
        if(array[i] == "$"){
            flag = true;
            break;
        }
        x = i;
        i = i*2;
    }

    // i is a position that has a $ 
    // it can be the first or end or a position in the $ array

    // pos gives 1st position of $
    int pos=  binarySearch(array, x, i, "$");
    int count = 1;

    if(pos == -1){
       cout << "5th $ not present" << endl;
        return 0;
    }

    while(array[pos] == "$"){
        count++;
        pos++;
        if(count == 5){
            break;
        }
    }

    if(count < 5){
        cout << "5th $ not present" << endl;
    }
    else{
        cout << "Position: "<< pos << endl;
    }

    return 0;
}