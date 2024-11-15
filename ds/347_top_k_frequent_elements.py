class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [ [] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for idx, val in count.items():
            freq[val].append(idx)

        res = []
        for i in range(len(freq) -1, 0, -1):
            for x in freq[i]:
                res.append(x)
                if len(res) == k:
                    return res