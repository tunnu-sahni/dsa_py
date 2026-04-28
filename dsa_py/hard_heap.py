# design twitter

import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        self.time = 0
        self.follow_map = defaultdict(set)
        self.tweets = defaultdict(list)
        # post tweet

    def postTweet(self, userId, tweetId):
        self.time += 1
        self.tweets[userId].append(self.time, tweetId)

# get news feed
    def getNewsFeed(self, userID):
        max_heap = []
        self.follow_map[userID].add(userID)
        for follower in self.follow_map[userID]:
            if follower in self.tweets:
                for time, tweetID in self.tweets[follower]:
                    heapq.heappush(max_heap, (-time, tweetID))
                    result = []
        while max_heap and len(result) < 10:
            result.append(heapq.heappop(max_heap)[1])
            return result
        # follow user

    def follow(self, followerID, followeeID):
        self.follow_map[followerID].add(followeeID)

        # unfollow user

    def unfollow(self, followerID, followeeID):
        if followeeID in self.follow_map[followerID]:
            self.follow_map[followerID].remove(followeeID)

