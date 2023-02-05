//int left = 0;
//         int right = nums.length - 1;
        
//         while (left <= right){
//             int mid = left + (right - left) / 2; // prevents overflow
//             System.out.println(left + "," + right);
//             if(nums[mid] == target){
                
//                 return true;
//             }
//             else if(nums[left] <= nums[mid]){
//                 if(nums[left] < target && target <= nums[mid]){
//                     right = mid - 1;
//                 }
//                 else{
//                     left = mid + 1;
//                 }
//             }
//             else{
//                 if (nums[mid] <= target && target < nums[right]){
//                     left = mid + 1;
//                 }
//                 else{
//                     right = mid - 1;
//                 }
//             }
//         }
//         return false;
class Solution {
    public boolean search(int[] nums, int target) {
        // trying the same approach as search in rotated sorted array 1
        // update: Doesn't work
        // trying finding the pivot method, hope it works
        // update: didn't work
        // using the two pointer approach 
        
        int left = 0, right = nums.length - 1;
        // edge case
        if (left == right && nums[left] == target){
            return true;
        }
        while (left <= right){
            if(nums[left] == target){
                return true;
            }
            if (nums[right] == target){
                return true;
            }
            left += 1;
            right --;
        }
        return false;
    }
}