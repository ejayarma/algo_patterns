import heapq
from collections import Counter

class Pair:
    def __init__(self, s: str, freq: int) -> None:
        self.s: str = s
        self.freq: int = freq
        
    
    def __lt__(self: Pair, other: Pair):
        if self.freq == other.freq:
            return self.s > other.s
        return self.freq < other.freq
    

def k_most_frequent_strings_max_heap(s: list[str], k: int) -> list[str]:
    frequencies = Counter(s)
    
    min_heap: list[Pair] = []
    for s_slice, s_freq in frequencies.items():    
        heapq.heappush(min_heap, Pair(s_slice, s_freq))
        
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    res = [heapq.heappop(min_heap).s for _ in range(k)]
    res.reverse()
    return res
