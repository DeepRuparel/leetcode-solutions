class Solution {
    /*
    Time = O(n)
    Soace = O(n)
    
    */
    public int[] shuffle(int[] nums, int n) {
       
        int [] ans = new int [nums.length];
        int j = 0;
        for(int i = 0; i < n; i++){
            ans[j] = nums[i];
            j++;
            ans[j] = nums[i+n];
            j++;
        }
        return ans;
    }
}