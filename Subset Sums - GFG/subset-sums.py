#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
		ans = []
        output = []
        def backtrack(start = 0, curr = []):
            ans.append(sum(curr[:]))
            #output.append(curr[:])
            for i in range(start , N):
                curr.append(arr[i])
                backtrack(i + 1, curr)
                curr.pop()
        
        #arr = sorted(arr)
        backtrack()
        #print(output)
        return ans
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends