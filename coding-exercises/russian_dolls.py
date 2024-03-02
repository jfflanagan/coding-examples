class Solution:
    def maxEnvelopes(self, envelopes):
        #sort by height
        envelopes.sort(key=lambda x: x[0], reverse=True)

        height_list = [x[1] for x in envelopes]

        #find maximum decreasing sequence: Use DP
        n = len(height_list)
        dp_table = [1] * n
        max_env = 1
        for j in range(1, n):
            for i in range(0, j):
                if height_list[j] < height_list[i] and envelopes[j][0] < envelopes[i][0]:
                    dp_table[j] = max(dp_table[i] + 1, dp_table[j])
                    max_env = max(max_env, dp_table[j])

        return max_env



#env = [[5,4],[6,4],[6,7],[2,3]]
#env = [[1,1],[1,1],[1,1]]
#
#env = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
#env = [[1,2],[2,3],[3,4],[3,5],[4,5],[5,5],[5,6],[6,7],[7,8]]