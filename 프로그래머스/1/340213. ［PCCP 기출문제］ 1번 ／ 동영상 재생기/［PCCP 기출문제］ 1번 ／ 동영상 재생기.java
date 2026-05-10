class Solution {
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        // 1. 시간 변환 (인덱스 3, 5 주의)
        int vLen = toSec(video_len);
        int curr = toSec(pos);
        int oStart = toSec(op_start);
        int oEnd = toSec(op_end);

        // 2. 시작하자마자 오프닝 체크
        if (curr >= oStart && curr <= oEnd) curr = oEnd;

        // 3. 명령어 수행
        for (String cmd : commands) {
            if (cmd.equals("next")) {
                curr = Math.min(vLen, curr + 10);
            } else if (cmd.equals("prev")) {
                curr = Math.max(0, curr - 10);
            }
            
            // 이동 후 다시 오프닝 체크
            if (curr >= oStart && curr <= oEnd) curr = oEnd;
        }

        // 4. "mm:ss" 형식으로 반환
        return String.format("%02d:%02d", curr / 60, curr % 60);
    }

    // 시간을 초로 바꿔주는 도우미 함수 (코드가 깔끔해집니다)
    private int toSec(String time) {
        int mm = Integer.parseInt(time.substring(0, 2));
        int ss = Integer.parseInt(time.substring(3, 5));
        return mm * 60 + ss;
    }
}