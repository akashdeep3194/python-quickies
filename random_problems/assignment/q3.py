from typing import *
class Solution:
    def solve(self,arr:List,s:str) -> bool:
        len_str = len(s)
        len_list = len(arr)
        if s == "":
            return True
        if len_list == 0:
            return False

        for i in range(len(s)):
            if s[:len_str - i] in arr:
                arr.remove(s[:len_str-i])
                if self.solve(arr,s[len_str-i:]):
                    return True
                arr.append(s[:len_str-i])
        return False
                
s = Solution()

if __name__ == '__main__':
    A = ['back' , 'end', 'front', 'tree']
    input_str = 'backend'
    print(s.solve(A,input_str))
