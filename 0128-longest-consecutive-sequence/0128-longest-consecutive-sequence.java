class Solution {
    public int longestConsecutive(int[] nums) {
        int longest = 0;
        Set<Integer> hashset = new HashSet<Integer>();
        for(int i = 0; i < nums.length; i++){
            hashset.add(nums[i]);
        }
        
        for(Integer num: hashset){
            if (!hashset.contains(num-1)){
                int currLongest = 1;
                int current = num;
                while(hashset.contains(current+1)){
                    current ++;
                    currLongest++;
                }
                longest = Math.max(currLongest, longest);
            }
        }
        return longest;
    }
}