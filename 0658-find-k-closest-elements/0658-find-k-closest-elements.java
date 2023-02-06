class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        List<Integer> ans = new ArrayList <Integer>();
        int left = 0;
        int right = arr.length - k;
        
        while (left < right){
            int mid = left + (right - left) / 2;
            if ( x - arr[mid] > arr[mid+k] -x){
                left = mid+1;
            }
            else{
                right = mid;
            }
        }
        arr = Arrays.copyOfRange(arr, left, left+k);
        for(int i = 0; i < arr.length; i++){
            ans.add(arr[i]);
        }
        return ans;
        
    }
}