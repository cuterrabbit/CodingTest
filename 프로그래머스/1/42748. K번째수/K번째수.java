import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        
        int[] answer = new int[commands.length];
        
        for (int i = 0; i < commands.length; i++) {
            int start = commands[i][0]; // i
            int end = commands[i][1];   // j
            int k = commands[i][2];     // k
            
            int[] elements = Arrays.copyOfRange(array, start - 1, end);
            
            Arrays.sort(elements);
            
            answer[i] = elements[k - 1];
        }
        
        return answer;
    }
}