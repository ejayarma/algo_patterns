from collections import defaultdict

def substring_anagrams(s: str, t: str) -> int:
    left = right = 0
    len_s, len_t = len(s), len(t)
    
    if len_t > len_s:
        return 0

    anagrams = 0
    expected_freq, window_freq = [0] * 26, [0] * 26
    for c in t:
        expected_freq[ord(c) - ord('a')] += 1
    while right < len_s:
        window_freq[ord(s[right]) - ord('a')] += 1
        if right - left + 1 == len_t:
            if window_freq == expected_freq:
                anagrams += 1
            window_freq[ord(s[left]) - ord('a')] -= 1
            left += 1
        right += 1
    return anagrams




def substring_anagrams_new(s: str, t: str) -> int:
    len_t, len_s = len(t), len(s)
    
    if len_t > len_s:
        return 0

    left = right = count = 0
    window_freq, expected_freq = [0] * 26, [0] * 26
    
    for c in t:
        expected_freq[ord(c) - ord('a')] += 1

    while right < len_s:
        if right - left + 1 == len_t: # window size met
            # process window
            # 
            left += 1
        # Keep moving right
        right += 1

    return count


print(substring_anagrams('caabab', 'aab'))
