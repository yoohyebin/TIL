class Solution {
    public int solution(String s) {
        return Integer.parseInt(s);
    }
}

/*
 * 다른 풀이
 * 입력받은 문자열을 끝까지 순회하며 현재 문자 하나씩 추출해 확인
 * - 만약 '-'가 나오면 Sign 변수를 false로 바꿔주고,
 * - 만약 '+'가 나오면 그냥 넘어감
 * - 만약 숫자가 나오면 문자 '0'을 빼서 정수로 변환 후 result에 10을 곱한 후 더해줌
 * - 마지막으로 Sign이 true면 result를 반환하고, false면 result에 -1을 곱한 후 반환
 */
class Solution2 {
    public int getStrToInt(String str) {
        boolean Sign = true;
        int result = 0;

      for (int i = 0; i < str.length(); i++) {
        char ch = str.charAt(i);

        if (ch == '-') {
            Sign = false;
        } else if(ch !='+')
            result = result * 10 + (ch - '0');
        }
        
        return Sign?1:-1 * result;
    }

    public static void main(String args[]) {
        Solution2 strToInt = new Solution2();
        System.out.println(strToInt.getStrToInt("-1234"));
    }
}