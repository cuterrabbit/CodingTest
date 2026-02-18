class Solution {
    public String solution(String number, int k) {
        StringBuilder answer = new StringBuilder();
        int idx = 0; // 탐색을 시작할 위치
        
        // 남겨야 할 숫자의 개수만큼 반복 (len - k)
        for (int i = 0; i < number.length() - k; i++) {
            char max = '0';
            // 현재 위치(idx)부터, 뒤에 남겨야 할 숫자들의 자리를 확보한 범위까지 탐색
            for (int j = idx; j <= k + i; j++) {
                if (max < number.charAt(j)) {
                    max = number.charAt(j);
                    idx = j + 1; // 찾은 큰 숫자 다음부터 다시 탐색
                }
            }
            answer.append(max);
        }
        return answer.toString();
    }
}