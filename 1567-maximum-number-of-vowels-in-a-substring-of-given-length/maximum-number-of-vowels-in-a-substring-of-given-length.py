class Solution(object):
    def maxVowels(self, s, k):
        vowels = {'a', 'e', 'i', 'o', 'u'}

        vowel_count = 0

        for ch in s[:k]:
            if ch in vowels:
                vowel_count += 1
                
        max_vowels = vowel_count

        left = 0

        for right in range(k, len(s)):

            if s[left] in vowels:
                vowel_count -= 1

            left += 1

            if s[right] in vowels:
                vowel_count += 1

            max_vowels = max(max_vowels, vowel_count)

        return max_vowels

        