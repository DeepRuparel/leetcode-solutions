class Solution {
    /*
    Approach: 
    Create a maxHeap and start adding elements
    If the size if greater than k we will remove the top most element and at the end the kth smallest element will be on top
    Time : O(m*n*logk) m is the number of rows, n is the no of columns
    Space : O(k) since only ke elments are kept in the heap.
    */
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