from typing import *  # type: ignore


class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        return '_'.join('#' + s.encode().hex() for s in strs)

    def decode(self, s: str) -> List[str]:
        if s == "": return []
        return [bytes.fromhex(e[1:]).decode() for e in s.split('_')]


class NeetSolution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res


obj = Solution()

encoded = obj.encode(["abc"])
print(encoded, type(encoded))
print(obj.decode(encoded))

encoded = obj.encode([])
print(encoded, type(encoded))
print(obj.decode(encoded))

encoded = obj.encode([""])
print(encoded, type(encoded))
print(obj.decode(encoded))

