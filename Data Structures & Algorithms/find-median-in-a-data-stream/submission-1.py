import heapq

class MedianFinder:

    def __init__(self):
       
        self.small = [] 
        
        # large: Min-Heap (stores larger half)
        self.large = []

    def addNum(self, num: int) -> None:
        # Step 1: Pehle default Max-Heap (small) mein push karo
        heapq.heappush(self.small, -1 * num)
        
        # Step 2: Ensure karo ki small ka max element <= large ka min element ho
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        # Step 3: Size Balance Check
        # small ki size large se 1 se zyada nahi honi chahiye
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        # large ki size small se badi nahi honi chahiye
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # Agar odd elements hain, toh small ka top hi median hai
        if len(self.small) > len(self.large):
            return float(-1 * self.small[0])
        
        # Agar even elements hain, toh dono heaps ke tops ka average
        return (-1 * self.small[0] + self.large[0]) / 2.0