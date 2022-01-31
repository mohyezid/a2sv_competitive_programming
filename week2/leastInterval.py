class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
             
        
            mapping = [0] * 26
            for i in tasks:
                mapping[ord(i) - ord("A")] += 1

            mapping.sort()
            f_max = mapping.pop()
            idle_time = (f_max - 1) * n

            while mapping and idle_time > 0:
                idle_time -= min(f_max - 1, mapping.pop())
            if idle_time<0:
                idle_time = 0 
            return idle_time + len(tasks)
