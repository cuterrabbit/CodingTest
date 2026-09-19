class Solution:
    def dailyTemperatures1(self, temperatures: list[int]) -> list[int]:
        output = []
        for i in range(len(temperatures)):
            stack, n = [], 0
            j = i
            while True:
                if j + 1 >= len(temperatures):
                    output.append(0)
                    break
                stack.append(temperatures[j])
                j += 1
                if stack[-1] >= temperatures[j]:
                    stack.append(temperatures[j])
                elif stack[-1] < temperatures[j]:
                    if temperatures[j] > temperatures[i]:
                        output.append(j - i)
                        break
                    else:
                        stack.pop()
        return output

    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans = [0] * len(temperatures)
        stack = []
        for day, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prev_day = stack.pop()[0]
                ans[prev_day] = day - prev_day
            stack.append((day, temp))
        return ans