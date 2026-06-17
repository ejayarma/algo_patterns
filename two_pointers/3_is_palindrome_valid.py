def is_palindrome_valid(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


print("", is_palindrome_valid("")) # empty string
print("a", is_palindrome_valid("a")) # single-character string
print("aa", is_palindrome_valid("aa")) # 2 characters
print("ab", is_palindrome_valid("ab")) # 
print("abba", is_palindrome_valid("abba")) # palindrome with 4 chars
print("!, (?)", is_palindrome_valid("!, (?)")) # string with no alphanum chars
print("12.02.2 021", is_palindrome_valid("12.02.2 021")) # palindrome with punctuation and nums
print("21.02.2 021", is_palindrome_valid("21.02.2 021")) # non-palindrome with punctuation and nums
print("hello, world I", is_palindrome_valid("hello, world I")) # non-palindrome with punctuation
print("a dog! a panic in a pagoda.", 
      is_palindrome_valid("a dog! a panic in a pagoda.") # long string palindrome
)
