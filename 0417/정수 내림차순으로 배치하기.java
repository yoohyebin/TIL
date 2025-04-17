import java.util.*;

class Solution {
    public long solution(long n) {
        long answer = 0;
        String[] list = String.valueOf(n).split("");
        Arrays.sort(list, Collections.reverseOrder());
        
        for(String val: list) {
            answer = answer*10 + Integer.parseInt(val);
        }
        
        return answer;
    }
}

/*
 * 다른 풀ㅣ
 * StringBuilder를 사용
 */
class Solution2 {
    public long solution(long n) {
        String[] arr = String.valueOf(n).split("");
        Arrays.sort(arr, Collections.reverseOrder());

        StringBuilder sb = new StringBuilder();
        for (String s : arr) {
            sb.append(s);
        }

        return Long.parseLong(sb.toString());
    }
}