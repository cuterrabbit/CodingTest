import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        // 첫 번째 자릿수를 Key로, 리스트로 담을 해시
        Map<Integer, List<String>> map = new HashMap<>();
        
        for (int num : numbers) {
            // 첫째 자릿수 k 구하기
            int k = 0;
            if (num >= 1000) { 
                k = num / 1000;
            } else if (num >= 100) {
                k = num / 100;
            } else if (num >= 10) {
                k = num / 10;
            } else {
                k = num;
            }
            
            // 해시에 k를 기준으로 그룹화하여 담기
            map.putIfAbsent(k, new ArrayList<>());
            map.get(k).add(String.valueOf(num));
        }

        // 높은 자릿수 순서대로 결과 조립
        StringBuilder sb = new StringBuilder();
        for (int i = 9; i >= 0; i--) {
            if (map.containsKey(i)) {
                List<String> list = map.get(i);
                
                list.sort((a, b) -> (b + a).compareTo(a + b));
                
                for (String s : list) {
                    sb.append(s);
                }
            }
        }

        String answer = sb.toString();

        
        if (answer.length() > 0 && answer.charAt(0) == '0') {
            return "0";
        }
        
        return answer;
    }
}