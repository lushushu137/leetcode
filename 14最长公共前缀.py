def longestCommonPrefix(self, strs):
    prefix = ''
    index = 0
    if len(strs) == 1:
        return strs[0]
    if len(strs) == 0:
        return ""

    while True:
        if index < len(strs[0]):
            v = strs[0][index]
        else:
            return prefix

        for item in strs:
            if index >= len(item):
                return prefix
            if v != item[index]:
                return prefix
        prefix += item[index]
        index += 1
    return prefix