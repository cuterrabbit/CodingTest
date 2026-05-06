import java.util.*;

class Solution {
    static int count = 0;
    
    public int solution(int[] numbers, int target) {
        count = 0;  // 초기화
        dfs(numbers, target, 0, 0);  // numbers, target을 파라미터로 넘김
        return count;
    }
    
    static void dfs(int[] numbers, int target, int index, int current) {
        if (index == numbers.length) {
            if (current == target) count++;
            return;
        }
        dfs(numbers, target, index + 1, current + numbers[index]);
        dfs(numbers, target, index + 1, current - numbers[index]);
    }
}