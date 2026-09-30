class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.tweets[userId].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        results = []

        users = self.following[userId] | {userId}
        for uid in users:
            if self.tweets[uid]:
                idx = len(self.tweets[uid]) - 1
                ts, tid = self.tweets[uid][idx]
                heapq.heappush(heap, (-ts, tid, uid, idx - 1))
        
        while heap and len(results) < 10:
            ts, tid, uid, idx = heapq.heappop(heap)
            results.append(tid)
            if idx >= 0: 
                ts2, tid2 = self.tweets[uid][idx]
                heapq.heappush(heap, (-ts2, tid2, uid, idx - 1))

        return results


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId) 

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId) 
