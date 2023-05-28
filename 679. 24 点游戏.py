from itertools import permutations

class Solution:
    def judgePoint24(self, cards: list[int]) -> bool:
        self.dp = {}
        self.twoNumberCache = {}
        for card in cards:
            self.dp[str(card)] = {card}
        possibleCombinations = permutations(cards, 4)
        for cardsCombination in possibleCombinations:
            possibleResult = self.countNumbers(cardsCombination)
            if 24 in list(map(lambda e: round(e, 3), possibleResult)):
                return True
        
        return False

    def countNumbers(self, cards: list[int]) -> set[int]:
        cardsKey = self.generateKey(cards)
        if cardsKey in self.dp:
            return self.dp[cardsKey]
        
        # first divide, 3 and 1
        resultSet = set()
        for i in range(1, len(cards)):
            frontCards = cards[0: i]
            backCards = cards[i: len(cards)]
            frontChildNumbers = self.countNumbers(frontCards)
            backChildNumbers = self.countNumbers(backCards)
            
            for num1 in frontChildNumbers:
                for num2 in backChildNumbers:
                    resultSet = resultSet.union(self.generatePossibility(num1, num2))
        self.dp[cardsKey] = resultSet
        return resultSet

    def generateKey(self, c: list[int]) -> str:
        return ",".join(map(str, c))
    
    def generatePossibility(self, num1: int, num2: int) -> set[int]:
        numsKey = self.generateKey([num1, num2])
        if numsKey in self.twoNumberCache:
            return self.twoNumberCache[numsKey]
        result = {
            num1 + num2,
            num1 - num2,
            num2 - num1,
            num1 * num2,
        }
        if num2 != 0:
            result.add(num1 / num2)
        if num1 != 0:
            result.add(num2 / num1)
        self.twoNumberCache[numsKey] = result
        return result

s = Solution()
cards = [3,3,8,8]
print(s.judgePoint24(cards))

# print(s.twoNumberCache["3,8"])