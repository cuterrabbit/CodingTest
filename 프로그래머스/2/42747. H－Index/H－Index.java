import java.util.Arrays;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        Arrays.sort(citations); 
        
        int k = 0; 
        for (int i = 0; i < citations.length; i++) {

            int h = citations.length - i; 


            if (citations[i] >= h) {

                if (h > k) {
                    k = h;
                }

                break; 
            }
        }
        
        answer = k;
        return answer;
    }
}