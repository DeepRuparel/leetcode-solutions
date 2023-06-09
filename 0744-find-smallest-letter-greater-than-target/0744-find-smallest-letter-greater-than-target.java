class Solution {
    /* 
    Approach:
    Doing a binary seach
    Time: O(logn)
    Space : O(1)
    */
    public char nextGreatestLetter(char[] letters, char target) {
        int low = 0;
        int high = letters.length;
        
        while (low < high){
            int mid = low + (high-low)/2; // to prevent overflow
            if(letters[mid] <= target){
                low = mid + 1;
            }
            else{
                high = mid;
            }
        }
        return letters[low % letters.length];
        
    }
}