class Solution {
    public String solution(String number, int k) {
        StringBuilder answer = new StringBuilder();
        int idx = 0;
        
        for (int i = 0; i < number.length() - k; i++) {
            char max = '0';
            
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