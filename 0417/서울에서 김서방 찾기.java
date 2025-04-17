import java.util.*;

class Solution {
    public String solution(String[] seoul) {
        String answer = "";
        
        for (int i=0; i<seoul.length; i++) {
            if (seoul[i].equals("Kim")) {
                return "김서방은 "+i+"에 있다";
            }
        }
        
        return answer;
    }
}

class Solution2 {
    public String solution(String[] seoul) {
        int index = Arrays.asList(seoul).indexOf("Kim");
        return "김서방은 " + index + "에 있다";
    }
}