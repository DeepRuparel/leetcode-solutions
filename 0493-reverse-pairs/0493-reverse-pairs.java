class Solution {
    static int merge(int[] nums, int low, int mid, int high){
        int cnt = 0;
        int j = mid + 1;  // initializing j at the starting position of the right half of the array
        for(int i= low;i<=mid;i++){    // iterate i in the left half of the array
            while(j<=high && nums[i]> (2 * (long) nums[j])){ // either right half is exausted or if condition in question turns out as false, keep incrementing the j pointer
                j++;
            }
            cnt+= (j-(mid+1));  // counting the number of left elements (how much j has moved from initial mid+1)
        }
		
		// now we simply perform the merge function 
		
        ArrayList<Integer> temp = new ArrayList<>();
        int left = low;
        int right = mid+1;
        while(left<=mid && right<=high){
            if(nums[left]<=nums[right]){ // adding the smaller to the temp arraylist
                temp.add(nums[left++]);  // incrementing the index of the added element
            }
            else{
                temp.add(nums[right++]); // adding and incrementing right if right is smaller
            }
        }
        while(left<=mid){    // if left part is left to be copied, we add it to the arraylist and increment index left
            temp.add(nums[left++]);
        }
        while(right<=high){   // if right part is left to be copied, we add it to the arraylist and increment index right
            temp.add(nums[right++]);
        }
        for(int i =low;i<=high;i++){
            nums[i] = temp.get(i-low);  // copying the sorted arraylist to the original nums array
        }
        return cnt;  // returing the total number of pairs
        
        
    }
    // public int countpairs(int[] nums, int left, int mid, int right){
    //     int count = 0;
    //     int r = mid + 1;
    //     for(int i = left; i <= mid; i++){
    //         while(r <= right && nums[i] > nums[r] * 2){
    //             r++;
    //         }
    //         count += (r - (mid + 1));
    //     }
    //     return count;
    // }
    
    public int mergesort(int[]nums, int left, int right){
        int count = 0;
        if (left >= right){
            return count;
        }
        int mid = left + (right - left)/2;
        count += mergesort(nums, left, mid);
        count += mergesort(nums, mid + 1, right);
        count += merge(nums, left, mid, right);
        //merge(nums, left, mid, right);
        return count;
    }
    public int reversePairs(int[] nums) {
        return mergesort(nums, 0, nums.length - 1);
        
    }
}