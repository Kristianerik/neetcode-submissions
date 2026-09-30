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

        heap = [(-ts, tid) for ts, tid in self.tweets[userId]]
        for followeeId in self.following[userId]:
            for ts, tid in self.tweets[followeeId]:
                heap.append((-ts, tid))
        heapq.heapify(heap)

        while heap and len(results) < 10:
            _, tweetId = heapq.heappop(heap)
            results.append(tweetId)

        return results


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId) 

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId) 
