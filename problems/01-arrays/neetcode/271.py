from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        enc_ascii = 31
        ascii_arr = []

        for s in strs:
            for char in s:
                ascii_arr.append(str(ord(char)))
            ascii_arr.append(str(enc_ascii))

        return "" if not strs else ",".join(ascii_arr)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        encryption_key = ","
        l = s.split(encryption_key)

        short_str, ret_arr = "", []
        for elem in l:
            if elem == "31":
                ret_arr.append(short_str)
                short_str = ""
            else:
                short_str += chr(int(elem))

        return ret_arr


sol = Solution()
strs = ["neet", "co'de", "love", "you"]
encodedStr = sol.encode(strs)
decodedStrs = sol.decode(encodedStr)
print(decodedStrs)

print(not ["1"])
