class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts = {}
        t_counts = {}
        either_contain = set()

        for char in s:
            either_contain.add(char)
            if char not in s_counts:
                s_counts[char] = 1
            else:
                s_counts[char] += 1

        for char in t:
            either_contain.add(char)
            if char not in t_counts:
                t_counts[char] = 1
            else:
                t_counts[char] += 1

        for char in either_contain:
            if char not in s_counts or char not in t_counts:
                return False
            if s_counts[char] != t_counts[char]:
                return False

        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []

        for s in strs:
            has_anagram_group = False
            
            for group in ret:
                if self.isAnagram(s, group[0]):
                    group.append(s)
                    has_anagram_group = True
                    break

            if not has_anagram_group:
                ret.append([s])
                
        return ret