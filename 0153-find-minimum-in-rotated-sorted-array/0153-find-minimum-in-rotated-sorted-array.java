class Solution {
    /*
    Brute force: To sort the array and return smallest item
    Time : O(nlogn)
    Space : O(n)
    
    Binary search approach 
    [3, 4, 5|, 1, 2]
                ^   
    [4, 5, 6, 7|, 0, 1, 2]
                 |   ^ |  
                 
    Time : O(logn)
    Space : O(n)
    */
    public int findMin(int[] nums) {
        
        
        while (nums.length != 1) {
            int left = 0 ; 
            int right = nums.length;
            int mid = left + (right -left)/2 ;  //prevents integer overflow
            int[] rightArr =  Arrays.copyOfRange(nums, mid,right);
            int [] leftArr = Arrays.copyOfRange(nums, left, mid);
            //System.out.println(Arrays.toString(leftArr));
            //System.out.println(Arrays.toString(leftArr));
            if(leftArr[leftArr.length - 1] > rightArr[rightArr.length - 1]){
                nums = rightArr;
            }else{
                nums = leftArr;
            }
        }
        return nums[0];
    }
}