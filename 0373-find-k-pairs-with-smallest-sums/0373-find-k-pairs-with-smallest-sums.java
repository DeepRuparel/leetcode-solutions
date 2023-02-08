class Solution {
    /*
    Brute force:
    2 for loops and store all the answers in a sorted form
    return top k
    Time : O(n*m)
    Space : O(m*n)
    ***Optimize it a bit
    note add min of k or len(nums2) for the loop to create heap
    create a heap using elements from the first array and the first element from second array
    then use while k > 0
    pop the first element 
    add it to ans 
    check length is less than len(nums2)
    if yes add
    current poped element and index+1 element and index +1 in heap
    */
    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        
        List<List<Integer>> pairs = new ArrayList<> ();
        if (nums1.length == 0 || nums2.length == 0 || k == 0) {
            return pairs;
        }
        // creating a min heap
        PriorityQueue<int[]> minHeap = new PriorityQueue<> ((arr1, arr2) -> arr1[0] + arr1[1] - arr2[0] - arr2[1]);
        // going over the min(k, len(muns1))
        int len = nums1.length;
        for (int i = 0 ; i < Math.min(k,len); i++){
            minHeap.offer(new int [] {nums1[i], nums2[0], 0});
        }
        while ((k--) > 0 && !minHeap.isEmpty()){
            int [] curr = minHeap.poll();
            List<Integer> temp = new ArrayList<Integer>();
            temp.add(curr[0]);
            temp.add(curr[1]);
            pairs.add(temp);
            // checking curr[2] + 1 < len(nums2)
            if ( curr[2] + 1 < nums2.length){
                // yes then add curr[0] and nums2[curr[2] + 1] and curr[2] + 1 in minHeap
                minHeap.offer(new int []{ curr[0], nums2[curr[2] + 1], curr[2]+1 });
            }
        }
        return pairs;
    }
}