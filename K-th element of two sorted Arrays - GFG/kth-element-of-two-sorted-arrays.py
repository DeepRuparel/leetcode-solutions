#User function Template for python3
import heapq
class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        
        h = []
        
        heapq.heappush(h, (arr1[0],1, 0))
        heapq.heappush(h, (arr2[0],2, 0))
        
        while k != 1:
            element, array, size = heapq.heappop(h)
            if array == 1:
                if size + 1 < len(arr1):
                    heapq.heappush(h, (arr1[size + 1],1, size + 1))
            else:
                if size + 1 < len(arr2):
                    heapq.heappush(h, (arr2[size + 1],2, size + 1))
            k -= 1
        
        element, array, size = heapq.heappop(h)
        return element
        
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m, k = sz[0], sz[1], sz[2]
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement( a, b, n, m, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends