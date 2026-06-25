from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringBruteForce(self, s: str) -> int:
        longest = 0
        n = len(s)
        for i in range(n):
            chars_set = set(s[i])
            for j in range(i + 1, n):
                if s[j] in chars_set:
                    break
                else:
                    chars_set.add(s[j])
            longest = max(longest, len(chars_set))
        return longest
    
    def lengthOfLongestSubstringSlidingWindow(self, s: str) -> int:
        max_length = 0
        left = 0
        right = 0
        chars_set = set()
        while right < len(s):
            if s[right] not in chars_set:
                chars_set.add(s[right])
                max_length = max(max_length, right - left + 1)
                right += 1
            else:
                chars_set.remove(s[left])
                left += 1
        return max_length
    
    def lengthOfLongestSubstringHashMap(self, s: str) -> int:
        start = 0
        chars_map = {}
        max_length = 0
        for i, c in enumerate(s):
            if c in chars_map and chars_map[c] >= start:
                start = chars_map[c] + 1
                max_length = max(max_length, i - start + 1)
            chars_map[c] = i
            print('i:', i, 'character:', c, 'start:', start, 'max_length;', max_length)
            print()
                
        return max_length


    

solve = Solution()

# print(solve.lengthOfLongestSubstringHashMap('au'))
print(solve.lengthOfLongestSubstringHashMap('abcabcbb'))
# print(solve.lengthOfLongestSubstringHashMap('bbbbb'))
# print(solve.lengthOfLongestSubstringHashMap('pwwkew'))
