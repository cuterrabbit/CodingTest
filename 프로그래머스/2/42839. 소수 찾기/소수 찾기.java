import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public int solution(String numbers) {
        List<String> result = new ArrayList<>();
        result.add("");
        for (char c : numbers.toCharArray()) {
            List<String> newResult = new ArrayList<>();
            for (String s : result) {
                for (int i = 0; i <= s.length(); i++) {
                    newResult.add(s.substring(0, i) + c + s.substring(i));
                }
            }
            result = newResult;
        }

        Set<Integer> set = new HashSet<>();               
        for (int i = 0; i < result.size(); i++) {
            String s = result.get(i);
            for (int len = 1; len <= s.length(); len++) { 
                set.add(Integer.parseInt(s.substring(0, len)));
            }
        }

        int answer = 0;
        for (int num : set) {
            if (num < 2) continue;                        
            int cnt = 0;
            for (int j = 1; j <= num; j++) {
                if (num % j == 0) {
                    cnt++;
                }
            }
            if (cnt == 2) {
                answer++;
            }
        }

        return answer;
    }
}