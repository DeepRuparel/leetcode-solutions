class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int duplicate = -1;
        for (int i= 0 ; i < nums.size(); i++){
            int index = abs(nums[i]);
            if(nums[index] < 0){
                duplicate = index;
                break;
            }
            nums[index] = -1*nums[index];   
        }
        
        //Restore the nums 
        for(auto& num:nums)
            num = abs(num);
        
        return duplicate;
    }
};