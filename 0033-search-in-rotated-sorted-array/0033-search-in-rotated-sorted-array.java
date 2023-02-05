class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        
        while (left <= right){
            int mid = left + (right - left) / 2;
            
            if (nums[mid] == target){
                return mid;
            }
            // check if the left element is less than the mid element whih means that part 
            //sorted and target can be found there.
            else if( nums[left] <= nums[mid]){
                // check if the target lies in the range left and mid
                // if so right = mid - 1
                // else left = mid + 1
                if( nums[left] <= target && target < nums[mid]){
                    right = mid - 1;
                }
                else{
                    left = mid + 1;
                }
            }
            else{
                if (nums[mid] < target && target <= nums[right]){
                    left = mid + 1; 
                }else{
                    right = mid - 1;
                }
            }
        }
        return -1;
    }
}