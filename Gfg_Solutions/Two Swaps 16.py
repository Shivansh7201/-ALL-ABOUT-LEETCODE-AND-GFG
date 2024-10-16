class Solution:
    def checkSorted(self, arr):
        c=0
        for i in range(1,len(arr)+1):
            if arr[i-1]!=i:
                idx=arr.index(i)
                arr[i-1],arr[idx]=arr[idx],arr[i-1]
                c+=1
            if c==2:
                return arr==sorted(arr)
        return arr==sorted(arr) #ff
