 #User function Template for python3
 
class Solution:
    
   #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        #code here
        num = set(arr)
        longest = 0
        for a in arr:
            if a-1 not in num:
                length = 1
                while a + length in num:
                    length += 1
                longest = max(longest,length)
        return longest
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        print(Solution().longestConsecutive(a))
        print("~")
# } Driver Code Ends