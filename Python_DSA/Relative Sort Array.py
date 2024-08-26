class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        result =[]

        for first in range(len(arr2)):
            for second in range(len(arr1)):
                if arr1[second]==arr2[first]:
                    result.append(arr1[second])
                    arr1[second] = -1 
        arr1.sort()

        for num in arr1:
            if num != -1:
                result.append(num)

        return result 

"""Please take care about the indentation while writing the code!!!"""

