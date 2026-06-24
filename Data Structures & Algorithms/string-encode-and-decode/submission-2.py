class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += f'{s}🫪'
        return ans



    def decode(self, s: str) -> List[str]:
        start_index = 0
        curr_index = 0

        ans = []

        while curr_index < len(s):
            if s[curr_index] == '🫪':
                ans.append(s[start_index:curr_index])
                start_index = curr_index + 1
            curr_index += 1

        
        return ans




            
