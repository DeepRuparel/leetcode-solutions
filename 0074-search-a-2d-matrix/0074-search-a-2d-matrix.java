class Solution {
    /*
    Brute force: scan the entire array
    Time O(n)^2
    Space: O(1)
    
    Binary search for optimized search
    Time O(logm*n)
    Space O(n)
    */
    public boolean searchMatrix(int[][] matrix, int target) {
        int left = 0, right = matrix[0].length, top = 0, bottom = matrix.length;
        
        while (left < right && top < bottom){
            if(matrix[top][right-1] == target){
                return true;
            }
            else if (matrix[top][right-1] > target){
                right--;
            }
            else{
                top++;
            }
        }
        return false;
    }
}