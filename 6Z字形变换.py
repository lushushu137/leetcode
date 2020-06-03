def convert(s, numRows):
    if numRows == 1:
        return s
    board = []
    x = 0
    y = 0
    down = True
    flag = True
    count = 0
    resDict = {}
    for i in range(numRows):
        resDict[i] = ''
    while flag:
        if down:
            while y < numRows:
                if count == len(s):
                    flag = False
                    break
                board.append((x, y))
                resDict[y] += s[count]
                y += 1
                count += 1
            down = False
            y -= 1
        if count == len(s):
            break
        if not down:
            while y > 0:
                if count == len(s):
                    flag = False
                    break
                x += 1
                y -= 1
                resDict[y] += s[count]
                count += 1
                board.append((x, y))

            down = True
            y += 1
        print(resDict)

    res = ''.join(resDict.values())
    # k = 0
    # while k < numRows:
    #     for index in range(len(board)):
    #         if board[index][1] == k:
    #             res += s[index]
    #     k += 1

    return res


print(convert("LEETCODEISHIRING", 3))
