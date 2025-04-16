class Solution {
    public int solution(int n) {
        int answer = 1;

        while(n % answer != 1){
            answer++;
        }
       
        return answer;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution(10));
    }
}