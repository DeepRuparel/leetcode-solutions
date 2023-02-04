class Solution {
    public int sumOfFlooredPairs(int[] nums) {
        HashMap<Integer, Integer> freq = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (freq.containsKey(nums[i])) {
                freq.put(nums[i], freq.get(nums[i]) + 1);
            } else {
                freq.put(nums[i], 1);
            }
        }
        //System.out.println(freq);
        int maximum = Arrays.stream(nums).max().getAsInt()+1;
        long [] prerodersum = new long [maximum];
        
        for (int i = 1; i < maximum; i++){
            if (freq.containsKey(i)){   
                prerodersum[i] = freq.get(i) + prerodersum[i-1];
            }
            else{
                prerodersum[i] = prerodersum[i-1];
            }
        }
        long summ = 0;
        Set<Integer> set = freq.keySet();
        for (Integer i : set) {
            for (int j = i; j < maximum; j += i){
                summ += freq.get(i)*(prerodersum[maximum-1]-prerodersum[j-1]);
            }
        }
        summ = summ % 1_000_000_007;
        return (int)summ;
    }
}