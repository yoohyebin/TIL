class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        
        for(int i=Math.min(a,b);i<=Math.max(a,b);i++){
            answer+=i;
        }
        
        return answer;
    }
}

/*
 * 다른 풀이
 * 등차수열의 합 공식 이용
 */

 class Solution2 {
    public long solution(int a, int b) {
        return sumAtoB(Math.min(a, b), Math.max(b, a));
    }

    private long sumAtoB(long a, long b) {
        return (b - a + 1) * (a + b) / 2;
    }
}