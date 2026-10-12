

class Solution:
    def combinationSum(self, candidates,target):
        candidates.sort()
        res = []
        sol = []

        def backtrack(start, curr_sum):
            if curr_sum == target:
                res.append(sol[:])
                return

            for i in range(start, len(candidates)):
                if curr_sum + candidates[i] > target:
                    break

                sol.append(candidates[i])
                backtrack(i, curr_sum + candidates[i])
                sol.pop()

        backtrack(0, 0)
        return res
