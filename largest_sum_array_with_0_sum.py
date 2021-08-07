'''
Largest subarray with 0 sum 
Easy Accuracy: 46.94% Submissions: 63476 Points: 2
Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.

Example 1:

Input:
N = 8
A[] = {15,-2,2,-8,1,7,10,23}
Output: 5
Explanation: The largest subarray with
sum 0 will be -2 2 -8 1 7.
Your Task:
You just have to complete the function maxLen() which takes two arguments an array A and n, where n is the size of the array A and returns the length of the largest subarray with 0 sum.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= N <= 105
-1000 <= A[i] <= 1000, for each valid i

link to question is : https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1
'''

def maxLen(n, arr):
    #Code here
    
    dict1={}
    sum1=0
    maxi=0
    for i in range(n):
        sum1+=arr[i]
        if(sum1==0):
            maxi=i+1
        else:
            if (sum1 in dict1.keys()):
                maxi=max(maxi,i-dict1[sum1])
            else:
                dict1[sum1]=i
    #print (maxi)
    return maxi
