class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Input array numbers = [1,2,3,4], target int = 3
        
        i = 0
        j = len(numbers) - 1

        while i < j:
            current = numbers[i] + numbers[j]
            if current == target:
                return [i + 1, j + 1]
            elif current < target:
                i += 1
            else:
                j -= 1
        
        return []
        #Output array [num1, num2] where num 1 + num 2 = target