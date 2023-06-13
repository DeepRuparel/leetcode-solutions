class Solution {
    public int maxSubArray(int[] nums) {
        int max1, max2;
        max1 = nums[0];
        max2 =  nums[0];
        
        for(int i = 1; i < nums.length; i++){
            max1 = Math.max(nums[i], nums[i] + max1);
            max2 = Math.max(max1, max2);
        }
        return max2;
        
    }
}