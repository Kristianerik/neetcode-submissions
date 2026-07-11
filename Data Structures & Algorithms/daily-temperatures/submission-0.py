class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Input temps = [30,38,30,36,35,40,28]
        stack = []
        output = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                idx = stack.pop()
                output[idx] = i -idx
            stack.append(i)
        
        return output

        #Output numDaysUntilWarmer = [1,4,1,2,1,0,0]