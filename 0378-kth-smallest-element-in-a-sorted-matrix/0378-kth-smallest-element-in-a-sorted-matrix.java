class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int m = matrix.length, n = matrix[0].length;
        //creating a maxheap
        PriorityQueue<Integer> heap = new PriorityQueue<>((a, b) -> Integer.compare(b,a));
        
        for(int i = 0; i < m ; i++){
            for(int j = 0; j < n; j++){
                heap.offer(matrix[i][j]);
                if(heap.size() > k){
                    heap.poll();
                }
            }
        }
        return heap.poll();
    }
}