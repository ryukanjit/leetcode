# Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of 
# one or more dictionary words. 
# For example, 
# given s = "leetcode", dict = ["leet", "code"]. Return true because "leetcode" can be segmented as "leet code".

def wordbreak(str, dict):
    return helper(str, dict, 0)

def helper(str, dict, start):
    if start == len(str):
        return True
    
    for word in dict:
        end = start + len(word)
        if (end > len(str)):
            continue 

        if (str[start: end] == word):
            if (helper(str, dict, end)):
                return True

    return False

s = "leetcodecoder"
dict = ["leet", "code", "coder"]

print(wordbreak(s, dict))