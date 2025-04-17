import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        List<Integer> result = new ArrayList<>();

        for (int num : arr) {
            if (num % divisor == 0) {
                result.add(num);
            }
        }

        if (result.isEmpty()) {
            return new int[]{-1};
        }

        Collections.sort(result);

        // List<Integer> → int[]로 변환
        int[] answer = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            answer[i] = result.get(i);
        }

        return answer;
    }
}

class Solution2 {
    public int[] solution(int[] arr, int divisor) {
        int[] answer = Arrays.stream(arr).filter(n -> n % divisor == 0).sorted().toArray();
        
        return answer.length == 0 ? new int[]{-1} : answer;
    }
}