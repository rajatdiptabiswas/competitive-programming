class Solution {
    public int numJewelsInStones(String J, String S) {
        
        int count = 0;
        
        for (char ch : S.toCharArray()) {
            if (J.indexOf(ch) >= 0)
                count += 1;   
        }
        
        // for (int i = 0; i < S.length(); i++) {
        //     if (J.contains(Character.toString(S.charAt(i))))
        //         count++;
        // }
        
        return count;
        
    }
}