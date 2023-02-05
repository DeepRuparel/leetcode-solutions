class Solution {
    /* sliding window approach wth a twist
    Time : O(n+m)
    Space: O(n)
    */
    public String minWindow(String s, String t) {
        
        if(s == null || t == null || s.isEmpty() || t.isEmpty()){
          return "";
        }
        
      // create a hashamp
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        for(int i = 0; i < t.length(); i++){
            char c = t.charAt(i);
            map.put(c, map.getOrDefault(c,0)+1);
        }
        int i = 0, j = 0, count = map.size();
        int left = 0, right = s.length() - 1, minSize = s.length();
        boolean found = false;
        while(j < s.length()){
            char end = s.charAt(j++);
            // check if end in hashmap
            if(map.containsKey(end)){
                map.put(end, map.get(end)-1);
                // check if it is now 0 if yes then decrement count
                if(map.get(end) == 0){
                    count--;
                }
            }
            if (count > 0){
                continue;
            }
            while (count == 0){
                char start = s.charAt(i++);
                if(map.containsKey(start)){
                    map.put(start, map.get(start) +1);
                    // check if it is now 0 if yes then decrement count
                    if(map.get(start) > 0){
                        count++;
                    }
                }
            }
            if ((j-i) < minSize){
                minSize = (j-i);
                left = i;
                right = j;
                found = true;
            }
        }
        if (found){
            return s.substring(left-1, right);
        }
        return "";
    }
}