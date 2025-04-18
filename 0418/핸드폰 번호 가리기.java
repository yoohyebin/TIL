class Solution {
    public String solution(String phone_number) {
        int len = phone_number.length();
        String stars = "*".repeat(len - 4);
        String lastFour = phone_number.substring(len - 4);
        return stars + lastFour;
    }
}

/*
 * 다른 풀이
 * Java 8 이하용 코드 (repeat 지원 안 될 때)
 */

 class Solution2 {
    public String solution(String phone_number) {
        int len = phone_number.length();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < len - 4; i++) {
            sb.append("*");
        }

        sb.append(phone_number.substring(len - 4));
        return sb.toString();
    }
}