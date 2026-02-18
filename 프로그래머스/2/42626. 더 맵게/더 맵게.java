import java.util.PriorityQueue;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> minHeap = new PriorityQueue<>(); // 최소 힙 생성
        for (int s : scoville) {
            minHeap.add(s);
        }

        // 힙의 가장 작은 값이 K보다 작을 때만 반복
        while (minHeap.peek() < K) {
            if (minHeap.size() < 2) {
                return -1;
            }

            int first = minHeap.poll();  
            int second = minHeap.poll(); 
            
            int mixed = first + (second * 2);
            minHeap.add(mixed); 
            
            answer++;
        }

        return answer;
    }
}