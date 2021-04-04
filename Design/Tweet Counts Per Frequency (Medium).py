# 1348. Tweet Counts Per Frequency - Medium
# Tags - Design

from collections import defaultdict
import bisect

class TweetCounts:

    def __init__(self):
        self.data = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort(self.data[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == 'minute':
            diff = 60
        elif freq == 'hour':
            diff = 3600
        else:
            diff = 86400
        
        res = []
        
        while startTime <= endTime:
            x = min(startTime + diff, endTime + 1)
            res.append(bisect.bisect_left(self.data[tweetName], x) - bisect.bisect_left(self.data[tweetName], startTime))
            startTime += diff
            
        return res


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)