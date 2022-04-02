# Finding the longest palindromic substring 
# is a classic problem of coding interview. 
# idea: start expanding from either (i, i) and (i, i + 1) from [0, len(str)]

def longestPalindrome(str):
    if len(str) == 0:
        return str
    
    if len(str) == 1:
        return str
    
    # start from first letter
    longest = str[0:1];
    for i in range(len(str)):
        tmp = helper(str, i , i)
        if len(tmp) > len(longest):
            longest = tmp
        
        tmp = helper(str, i , i + 1)
        if len(tmp) > len(longest):
            longest = tmp
        
    return longest 

def helper(str, begin, end):
    while begin >= 0 and end <= len(str) - 1 and str[begin:begin + 1] == str[end: end + 1]:
        begin -= 1
        end += 1
    
    return str[begin + 1: end]

print(longestPalindrome("ABCDEFEDCADGFSDFFABCDEFEDCBA"))
