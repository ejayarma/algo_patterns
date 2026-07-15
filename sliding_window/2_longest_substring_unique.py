def longest_substring_unique_mine(s: str) -> int:
    n = len(s)
    left = right = max_len = 0
    char_set: set[str] = set()
    while right < n:
        if s[right] not in char_set:
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)
            right += 1
        else:
            char_set.remove(s[left])
            left += 1
            
    return max_len

def longest_substring_unique(s: str) -> int:
    max_len = left = right = 0
    hash_set = set()
    while right < len(s):
        while s[right] in hash_set:
            hash_set.remove(s[right])
            left += 1
        max_len = max(max_len, right - left + 1)
        hash_set.add(s[right])
        right += 1
    return max_len

def longest_substring_unique_improved(s: str) -> int:
    max_len = left = right = 0
    prev_indexes = {}
    while right < len(s):
        while s[right] in prev_indexes and prev_indexes[s[right]] >= left:
            left = prev_indexes[s[right]] + 1
        max_len = max(max_len, right - left + 1)
        prev_indexes[s[right]] = right
        right += 1
    return max_len

print(longest_substring_unique('abcba'))
print(longest_substring_unique('cabcdeca'))
