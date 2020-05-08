# Problem Statement

 Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

### Examples:

```
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
```

### Note: You may assume the string contain only lowercase letters. 


# Solution

| Approach | Time Complexity |
|----------|:----------------|
| Naive    |   O (n^2)         |
| Using dictionary |  O(n)   |