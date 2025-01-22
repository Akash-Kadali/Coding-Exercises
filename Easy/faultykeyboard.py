class Solution:
    def finalString(self, s: str) -> str:
        words = s.split("i")
        new_word = ""
        for word in words:
            new_word += word
            new_word = new_word[::-1]
        return new_word[::-1]