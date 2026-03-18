class Solution {
    public int solution(int[][] sizes) {
        int maxGaro = 0;
        int maxSero = 0;

        for (int i = 0; i < sizes.length; i++) {
            
            int big   = Math.max(sizes[i][0], sizes[i][1]);
            int small = Math.min(sizes[i][0], sizes[i][1]);

            maxGaro = Math.max(maxGaro, big);
            maxSero = Math.max(maxSero, small);
        }
        int answer = maxGaro * maxSero;
        return answer;
    }
}