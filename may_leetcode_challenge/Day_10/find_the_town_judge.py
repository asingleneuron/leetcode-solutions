class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trust_count = collections.defaultdict(int)
        set_a = set()
        set_b = set(range(1, N + 1))

        for i in trust:
            trust_count[i[1]] += 1
            set_a.add(i[0])

        for eligible_town_judge in set_b - set_a:
            if trust_count[eligible_town_judge] == N - 1:
                return eligible_town_judge

        return -1


