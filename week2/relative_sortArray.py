class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i=0
        list_one=[]
        list_two=[]
        i=0
        while i<len(arr2):
            for j in arr1:
                if j == arr2[i]:
                    list_one.append(arr2[i])
            i+=1
        list_two=sorted([item for item in arr1 if item not in arr2])
        return list_one+list_two
