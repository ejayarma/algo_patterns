import heapq
from collections import Counter

class Pair:
    def __init__(self, s: str, freq: int) -> None:
        self.s = s
        self.freq = freq
        
    
    def __lt__(self: Pair, other: Pair):
        if self.freq == other.freq:
            return self.s < other.s
        return self.freq > other.freq
    

def k_most_frequent_strings_max_heap(s: list[str], k: int) -> list[str]:
    frequencies = Counter(s)
    
    max_heap = [Pair(s_slice, s_freq) for s_slice, s_freq in frequencies.items()]
    heapq.heapify(max_heap)
    return [heapq.heappop(max_heap).s for _ in range(k) ]
