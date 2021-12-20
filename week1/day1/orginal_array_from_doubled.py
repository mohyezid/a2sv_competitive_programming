class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        list = []
        list2 = deque()

        for num in sorted(changed):
            if list2 and num == list2[0]:
                list2.popleft()
            else:
                 list2.append(num * 2)
                 list.append(num)

        if list2:
             return []
        else:
            return list
