class Solution {
    public int solution(String name) {
        int answer = 0;
        int n = name.length();

        // 1. 상하 이동 
        for (int i = 0; i < n; i++) {
            char target = name.charAt(i);
            answer += Math.min(target - 'A', 'Z' - target + 1);
        }

        // 2. 좌우 이동 
        int move = n - 1; 

        for (int i = 0; i < n; i++) {
            
            int next = i + 1;
            while (next < n && name.charAt(next) == 'A') {
                next++;
            }

            // 시나리오 A: 오른쪽으로 가다가 왼쪽으로 꺾기
            int case1 = i * 2 + (n - next);

            // 시나리오 B: 처음부터 왼쪽(뒤)으로 먼저 갔다가 다시 오른쪽으로 꺾기
            int case2 = (n - next) * 2 + i;

            // 기존 move와 시나리오 A, B 중 가장 작은 값을 선택하여 갱신
            move = Math.min(move, Math.min(case1, case2));
        }

        return answer + move;
    }
}