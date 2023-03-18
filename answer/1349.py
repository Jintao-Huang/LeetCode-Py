from leetcode_alg import *


class Solution:
    """recommended. 二部图"""

    def maxStudents(self, seats: List[List[str]]) -> int:
        n, m = len(seats), len(seats[0])
        graph: List[List[int]] = [[] for _ in range(n*m)]
        cnt = 0
        for i, sl in enumerate(seats):  # seat_list
            for j, c in enumerate(sl):  # char
                if c == "#":
                    continue
                cnt += 1
                gn = i*m+j
                is_odd = j % 2
                if is_odd:
                    continue
                if i > 0:
                    if j > 0 and seats[i-1][j-1] == ".":
                        graph[gn].append(gn-m-1)
                    if j < m-1 and seats[i-1][j+1] == ".":
                        graph[gn].append(gn-m+1)
                # 只需保存向左的, 向右为冗余
                if j > 0 and seats[i][j-1] == ".":
                    graph[gn].append(gn-1)
                if j < m-1 and seats[i][j+1] == ".":
                    graph[gn].append(gn+1)
                if i < n-1:
                    if j > 0 and seats[i+1][j-1] == ".":
                        graph[gn].append(gn+m-1)
                    if j < m-1 and seats[i+1][j+1] == ".":
                        graph[gn].append(gn+m+1)
        return cnt - hungarian(graph)


class Solution2:
    def maxStudents(self, seats: List[List[str]]) -> int:
        n, m = len(seats), len(seats[0])
        dinic = Dinic(n*m+2)
        s, t = n*m, n*m+1
        cnt = 0
        for i, sl in enumerate(seats):  # seat_list
            for j, c in enumerate(sl):  # char
                if c == "#":
                    continue
                cnt += 1
                gn = i*m+j
                is_odd = j % 2
                if is_odd:
                    dinic.add_edge(gn, t, 1)
                    continue
                dinic.add_edge(s, gn, 1)
                if i > 0:
                    if j > 0 and seats[i-1][j-1] == ".":
                        dinic.add_edge(gn, gn-m-1, 1)
                    if j < m-1 and seats[i-1][j+1] == ".":
                        dinic.add_edge(gn, gn-m+1, 1)
                # 只需保存向左的, 向右为冗余
                if j > 0 and seats[i][j-1] == ".":
                    dinic.add_edge(gn, gn-1, 1)
                if j < m-1 and seats[i][j+1] == ".":
                    dinic.add_edge(gn, gn+1, 1)
                if i < n-1:
                    if j > 0 and seats[i+1][j-1] == ".":
                        dinic.add_edge(gn, gn+m-1, 1)
                    if j < m-1 and seats[i+1][j+1] == ".":
                        dinic.add_edge(gn, gn+m+1, 1)
        return cnt - dinic.run(s, t)


if __name__ == "__main__":
    seats = [["#", ".", "#", "#", ".", "#"],
             [".", "#", "#", "#", "#", "."],
             ["#", ".", "#", "#", ".", "#"]]
    assert Solution().maxStudents(seats) == 4
    assert Solution2().maxStudents(seats) == 4
