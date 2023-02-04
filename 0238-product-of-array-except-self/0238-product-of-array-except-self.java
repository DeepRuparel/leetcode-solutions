class Solution {
    /*
    Brute force
    Time : O(n)^2
    Space : O(n)
    
    iterate over the array using 2 for loops and answer it
    gives TLE
    
    Optimized:
    Time: O(n)
    Space: O(n)
    
    [1,1,1,1]
    prefix and postifx sum
    initilaize the array with product of previous nums
    then start the postfix from reverse and multiply the postfix with the res and change postfix to postix * nums[i]
    
    */
    public int[] productExceptSelf(int[] nums) {
        int [] result = new int [nums.length];
        for(int i = 0; i < result.length; i++){
            result[i] = 1;
        }
        int prefix = 1;
        for(int i = 0; i < result.length; i++){
            result[i] = prefix;
            prefix *= nums[i];
        }
        int postfix = 1;
        for(int i = result.length -1; i >= 0; i--){
            result[i] *= postfix;
            postfix *= nums[i];
        }
        return result;
            
    }
}