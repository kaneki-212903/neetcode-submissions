from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wlist=set(wordList)
        q=deque()
        q.append([beginWord,1])
        if endWord not in wlist:
            return 0
        while q:
            word,step=q.popleft()
            if word==endWord:
                return step
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    new_word=word[:i]+ch+word[i+1:]
                    if new_word in wlist:
                        q.append([new_word,step+1])
                        wlist.remove(new_word)
        return 0