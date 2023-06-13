class Solution {
    public int equalPairs(int[][] grid) {
        
        int count = 0;
        int n = grid.length;
        
        Map<String, Integer> d = new HashMap<>();
        for(int [] row : grid){
            String rowString = Arrays.toString(row);
            d.put(rowString, 1 + d.getOrDefault(rowString, 0));
        }
        
        for(int c = 0; c < n; c++){
            int [] colArray = new int[n];
            for (int r = 0; r < n; r ++){
                colArray[r] = grid[r][c];
            }
            String colString = Arrays.toString(colArray);
            count += d.getOrDefault(colString, 0);
        }
        
        return count;
        
    }
}