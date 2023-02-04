class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int left = 0;
        int right = matrix[0].length;
        int top = 0;
        int bottom = matrix.length;
        List<Integer> ans = new ArrayList<Integer>();
        while(left < right && top < bottom){
            //printing from left to right
            for(int i = left; i < right; i++){
                ans.add(matrix[top][i]);
            }
            top++;
            //printing from top to bottom
            for(int i = top; i < bottom; i++){
                ans.add(matrix[i][right-1]);
            }
            right--;
            //checking if left and top haven't crossed right and bottom respectively
            if (!(left < right && top < bottom)){
                break;
            }
            // printing from right to left
            for(int i = right -1; i > left -1; i--){
                ans.add(matrix[bottom-1][i]);
            }
            bottom--;
            //printing from bottom to top
            for(int i = bottom-1; i > top -1; i--){
                ans.add(matrix[i][left]);
               
            }
            left++;
            
        }
        return ans;
    }
}