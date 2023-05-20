class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if s == "" or len(words) == 0:
            return []
        wordsTree = {}
        result = []
        for word in words:
            cursor = wordsTree
            for i in range(len(word)):
                c = word[i]
                if i < len(word) - 1:
                    if c not in cursor:
                        cursor[c] = {}
                    cursor = cursor[c]
                else:
                    if c not in cursor:
                        cursor[c] = {
                            "countInWords": 0,
                            "countInS": 0,
                            "windowStartIndex": -1, # while window is sliding, we'll count different numbers for different start index
                        }
                    cursor[c]["countInWords"] += 1 
        windowSize = len(words) * len(words[0])
        for i in range(0, len(s) - windowSize + 1):
            clip = s[i:i + windowSize]
            cursor = wordsTree
            loopSuccess = True
            for c in clip:
                # new words, exit
                if c not in cursor:
                    loopSuccess = False
                    break
                # match the last character:
                if "countInWords" in cursor[c]:
                    if cursor[c]["windowStartIndex"] < i:
                        cursor[c]["windowStartIndex"] = i
                        cursor[c]["countInS"] = 1
                    elif cursor[c]["windowStartIndex"] == i:
                         cursor[c]["countInS"] += 1
                    else:
                        # should throw error
                        pass
                    # got more words in current sliding window than in words, fail
                    if cursor[c]["countInS"] > cursor[c]["countInWords"]:
                        loopSuccess = False
                        break
                    # alread in the last layer, go to top
                    cursor = wordsTree
                    continue
                # cursor move forward, prepare to check next charactor
                cursor = cursor[c]
            if loopSuccess:
                result.append(i)
        return result

s = Solution()
print(s.findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"]))