class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> hash = new HashMap<>();
        
        for(int num: nums){
            hash.put(num, 1 + hash.getOrDefault(num, 0));
            if(hash.get(num) > nums.length / 2){
                return num;
            }
        }
        return -1;
        
    }
}