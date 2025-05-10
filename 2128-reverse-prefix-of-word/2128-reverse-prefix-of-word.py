class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        x=0
        for i in range(len(word)):
            if word[i]==ch:
                x=i
                break
        print(x)
        return word[0:x+1][::-1]+word[x+1:]
        