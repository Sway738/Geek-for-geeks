#User function Template for python3
class Solution:
    
    def findMaxSum(self,n,m,mat):
        ans = -1
        
        for i in range(n-2):
            for j in range(m-2):
                curAns  = mat[i][j] + mat[i][j+1] + mat[i][j+2]
                curAns += + mat[i+1][j+1]
                curAns += mat[i+2][j] + mat[i+2][j+1] + mat[i+2][j+2]
                
                ans = max(ans, curAns)
                
        return ans

