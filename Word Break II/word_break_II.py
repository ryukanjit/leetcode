# Given a string s and a dictionary of words dict, add spaces in s to construct a sentence
# where each word is a valid dictionary word. Return all such possible sentences.
# For example, given s = "catsanddog", dict = ["cat", "cats", "and", "sand", "dog"], the solution is ["cats and dog", "cat sand dog"].

# idea: track the words 

def wordbreakII(str, dict):

    dp = [None for _ in range(len(str) + 1)]
    dp[0] = []

    for i in range(len(str)):
        if dp[i] == None:
            continue

        for word in dict:
            end = i + len(word)
            if str[i: end] == word:
                if dp[end] == None:
                    dp[end] = []
                
                dp[end].append(word)

    # print(dp)
    result = []
    if (dp[len(str)] == None):
        return result 
    
    temp = []
    dfs(dp, len(str), result, temp)
    return result 

def dfs(dp, end, result, tmp):
    # print(tmp)
    if end <= 0:
        path = tmp[(len(tmp) - 1)]
        for i in range(len(tmp) - 2, -1, -1):
            path += " " + tmp[i]
        
        result.append(path)
        return
    
    for str in dp[end]:
        tmp.append(str)
        dfs(dp, end - len(str), result, tmp)
        tmp.pop()

str = "catsanddog"
dict = ["cat", "cats", "and", "sand", "dog"]
print(wordbreakII(str, dict))