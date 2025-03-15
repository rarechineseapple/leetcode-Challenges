class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common = ""
    
        for i in range(len(strs[0])):  # loops through first string
            char = strs[0][i]  # current character
            for word in strs[1:]:  # compare with other
                if i >= len(word) or word[i] != char:  # stop on mismatch
                    return common
            common += char  # if matching add to common
    
        return common

        
        # prefix = strs[0]

        # for i in strs[1:]:  
        #     while not i.startswith(prefix):
        #         prefix = prefix[:-1] 
        #         if not prefix:
        #             return ""
        
        # return prefix
        # Longest Common Prefix

