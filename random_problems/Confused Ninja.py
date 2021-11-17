from typing import *

def confusedNinja(s: str)-> str:
    cz = cn = 0    
    for ele in s:
        if ele == "z":
            cz+=1
        if ele == "n":
            cn+=1
    ans = ""
    ans = "1"*cn+"0"*cz
    ans = int(ans)
    return ans

print(confusedNinja("oenorezeno"))
