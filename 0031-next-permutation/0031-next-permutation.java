class Solution {
    public void nextPermutation(int[] nums) {
        if (nums == null || nums.length <= 1){
            return;
        }
        int first = -1;
        int n = nums.length;
        
        for (int i = n - 2 ; i > -1; i--){
            if (nums[i] < nums[i + 1]){
                first = i;
                //System.out.print(first);
                break;
            }
        }
        if (first == -1){
            int temp;
            for (int i = 0; i < n/ 2; i ++){
                temp = nums[i];
                nums[i] = nums[n-i-1];
                nums[n-i-1] = temp;
            }
            return;
        }
        int l = n - 1;
        while (l > first){
            if (nums[first] < nums[l]){
                break;
            }
            l--;
        }
        //System.out.println(l);
        int temp = nums[first];
        nums[first] = nums[l];
        nums[l] = temp;
        //System.out.println(Arrays.toString(nums));
        first = first + 1;
        //System.out.print(first);
        while(first < n){
            temp = nums[first];
            nums[first] = nums[n - 1];
            nums[n - 1] = temp;
            first++;
            n--;
        }
    }
}
