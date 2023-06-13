class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        List<Integer>firstRow = new ArrayList<Integer>();
        firstRow.add(1);
        ans.add(firstRow);
        int size = 1;
        for(int i = 1; i < numRows; i++){
            List<Integer>row = new ArrayList<Integer>();
            row.add(1);
            for (int j = 1 ; j < size ; j ++){
                row.add(ans.get(i - 1).get(j-1) + ans.get(i-1).get(j));
            }
            row.add(1);
            ans.add(row);
            size++;
        }
        return ans;
        
        
        
    }
}