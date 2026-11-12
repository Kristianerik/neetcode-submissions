class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = {}
        for card in hand:
            count[card] = count.get(card, 0) + 1

        for start in sorted(count):
            n = count[start]
            if n == 0:
                continue
            for card in range(start, start + groupSize):
                if count.get(card, 0) < n:
                    return False
                count[card] -= n
        
        return True
            
        