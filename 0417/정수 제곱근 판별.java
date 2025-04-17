class Solution {
    public long solution(long n) {
        double sqrtVal = Math.sqrt(n);
        
        if (sqrtVal % 1 == 0) {
            return (long) Math.pow(sqrtVal+1, 2);
        }
        
        return -1;
    }
}