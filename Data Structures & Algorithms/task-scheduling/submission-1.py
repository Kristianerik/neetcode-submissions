class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        current_cycle = 0

        for task in tasks:
            count[task] = count.get(task, 0) + 1
        
        heap = [-c for c in count.values()]
        heapq.heapify(heap)

        cooldown_queue = deque()

        while heap or cooldown_queue:
            current_cycle += 1

            if cooldown_queue and cooldown_queue[0][1] <= current_cycle:
                freq, _ = cooldown_queue.popleft()
                if freq < 0:
                    heapq.heappush(heap, freq)

            if heap: 
                freq = heapq.heappop(heap)
                if freq + 1 < 0:
                    cooldown_queue.append((freq + 1, current_cycle + n + 1))


        return current_cycle