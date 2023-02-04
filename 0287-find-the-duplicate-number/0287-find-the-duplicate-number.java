class Solution {
    /*
    Bruet force : Create a hashmap and go through the frequencies
    Time : O(n)
    Space: O(n)
    
    Optimized way:
    Two pointers 
    [1,3, 4,2,2]
          ^ ^
    Time; O(n)
    Spacel O(1)
    Didn't work 2 pointers 
    
    Negative mraking 
    have a duplicate = -1 
    multiply the index with -1 before doing that check if it is less than 0, if so means it was 
    marked by a previous index and this element is duplicate
    Time; O(n)
    Spacel O(1)
    
    
    */
    public int findDuplicate(int[] nums) {
        int duplicate = -1;
        for (int i = 0; i< nums.length; i++){
            int curr = Math.abs(nums[i]);
            if (nums[curr] < 0){
                duplicate = curr;
                break;
            }
            nums[curr] *= -1;
        }
        for (int i = 0; i< nums.length; i++){
            nums[i] = Math.abs(nums[i]);
        }
        return duplicate;
    }
}