from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in anagrams_map:
                anagrams_map[sorted_word] = [word]
            else:
                anagrams_map[sorted_word] += [word]
        return [anagrams_map[key] for key in anagrams_map.keys()]



def main():
    sol = Solution()
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(sol.groupAnagrams(words))


if __name__ == '__main__':
    main()
