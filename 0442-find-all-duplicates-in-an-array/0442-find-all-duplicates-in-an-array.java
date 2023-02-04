class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> ans = new ArrayList<Integer>();
        for(int i = 0; i < nums.length; i++){
            int curr = Math.abs(nums[i])-1;
            //System.out.println(curr);
            if (nums[curr] < 0){
                ans.add(curr+1);
            }
            else{
                nums[curr] *= -1;
            }
        }
        for(int i = 0; i < nums.length; i++){
            nums[i] = Math.abs(nums[i]);
        }
        return ans;
        
    }
}