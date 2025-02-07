class Solution(object):
    def queryResults(self, limit, queries):
        """
        Finds the number of distinct colors among balls.
        Processes list of queries that assign colors to balls.
        :type limit: int - Number of balls + 1
        :type queries: List[List[int]] - A list where each sublist contains two integers [x, y]

        Returns:
        :rtype: List[int] - A list where each element represents the number of distinct colors after each iteration.
        """

        ball_to_color = {}  # map ball to color
        color_count = {}  # track balls with color
        distinct_color = 0  # counter for distinct colors
        result = []  # stores answer after each iteration

        #x and y are integers in each sublist within the queries list
        for x, y in queries:
            # get prev color of ball x where x is ball number
            # if ball is not colored yet, prev_color = None
            # otherwise prev_color = that color
            prev_color = ball_to_color.get(x, None)

            # Step 1: if ball has same color as before, skip processing
            if prev_color == y:
                result.append(distinct_color)
                continue

            # Step 2: remove previous color (if exists)
            if prev_color is not None and prev_color != y:
                color_count[prev_color] -= 1
                if color_count[prev_color] == 0:
                    del color_count[prev_color] # remove it from color_count
                    distinct_color -= 1  # remove color from distinct count

            # Step 3: assign new color to the ball
            ball_to_color[x] = y

            # Step 4: update the color count
            if y in color_count: # color already exists
                color_count[y] += 1
            else: # new color
                color_count[y] = 1
                distinct_color += 1  # new color added

            # append the current distinct color count to the result list
            result.append(distinct_color)

        return result


#sol = Solution()

#queries = [[1, 2], [2, 3], [1, 3], [3, 2]]

#total = sol.queryResults(4, queries)
#print(total)
