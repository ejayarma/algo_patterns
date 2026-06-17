def next_lexicographical_sequence_mine(s: str) -> str:
    letters = list(s)
    right = len(letters) - 1
    pivot = len(letters) - 2
   
    while pivot >= 0 and letters[pivot] >= letters[pivot + 1]:
        pivot -= 1
        
    if pivot == -1:
        return ''.join(reversed(letters))     
    
    while letters[right] < letters[pivot]:
        right -= 1
    
    letters[pivot], letters[right] = letters[right], letters[pivot]
    
    letters[pivot + 1:] = list(reversed(letters[pivot + 1:]))
    return ''.join(letters)

print('a', next_lexicographical_sequence_mine('a'))
print('aaaa', next_lexicographical_sequence_mine('aaaa'))
print('ynsdeit', next_lexicographical_sequence_mine('ynsdeit'))
print('abcedda', next_lexicographical_sequence_mine('abcedda'))
