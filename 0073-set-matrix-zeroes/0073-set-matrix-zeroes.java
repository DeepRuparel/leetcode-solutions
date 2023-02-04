class Solution {
    /*
    Approach:
    have 2 sets for x and y 
    as soon as you see a 0 add x in setx and y in set y
    then go through the array again and if it is x or y make that 0
    
    Time : O(n)^2
    Space: O(n)
    
    */
    public void setZeroes(int[][] matrix) {
        Set<Integer> setx = new HashSet<Integer>();
        Set<Integer> sety = new HashSet<Integer>();
        
        for(int i = 0 ; i < matrix.length; i++){
            for(int j = 0; j < matrix[0].length; j++){
                if (matrix[i][j] == 0){
                    setx.add(i);
                    sety.add(j);
                }
            }
        }
        for(int i = 0 ; i < matrix.length; i++){
            for(int j = 0; j < matrix[0].length; j++){
                if (setx.contains(i) || sety.contains(j)){
                    matrix[i][j] = 0;
                }
            }
        }
    }
}