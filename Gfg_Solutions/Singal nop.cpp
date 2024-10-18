// User function template for C++
/*Given an array arr[] of positive integers where every element appears even times except for one. Find that number occurring an odd number of times.

Examples:

Input: arr[] = [1, 1, 2, 2, 2]
Output: 2
Explanation: In the given array all element appear two times except 2 which appears thrice.
Input: arr[] = [8, 8, 7, 7, 6, 6, 1]
Output: 1
Explanation: In the given array all element appear two times except 1 which appears once.*/

class Solution {
  public:
    int getSingle(vector<int>& arr) {
        int  res=arr[0];
        for(int i=1;i<arr.size();i++){
            res=res^arr[i];
        }
        return res;
    }
};
