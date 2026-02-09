import java.util.HashMap;

class Solution {
    public int solution(String[][] clothes) {
        HashMap<String, Integer> hashMap = new HashMap<>();
        // 카테고리별로 몇 개가 있는지가 중요
        
        for (String[] cloth: clothes) {
            String category = cloth[1];
            
            hashMap.put(category, hashMap.getOrDefault(category, 0) + 1);
            // 찾는 key가 존재하면 해당 key에 매핑되어 있는 값을 반환, 그렇지 않으면 디폴트 값이 반환
        }   // 각 카테고리 별, 옷이 생성됨
        
        int answer = 1;
        for (int count : hashMap.values()){
            answer *= (count + 1);
        }
            
        return answer - 1;
    }
}