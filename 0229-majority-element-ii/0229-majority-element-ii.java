class Solution {
    public List<Integer> majorityElement(int[] nums) {
        HashMap<Integer, Object[]> map = new HashMap<>();
        List<Integer> ans = new ArrayList<>();
        for(int num : nums){
            if(map.containsKey(num)){
                int frequency = (int)map.get(num)[0];
                boolean present = (boolean)map.get(num)[1];
                frequency++;
                if(frequency > nums.length/3 && present == false){
                    ans.add(num);
                    map.put(num, new Object[] {frequency, true});
                }
                else{
                    map.put(num, new Object[] {frequency, present});
                                    
                }
            }
            else{
                int frequency = 1;
                if(frequency > nums.length/3){
                    ans.add(num);
                    map.put(num, new Object[] {frequency, true});
                }
                else{
                    map.put(num, new Object[] {frequency, false});
                }
            }
            
        }
        return ans;
        
    }
}