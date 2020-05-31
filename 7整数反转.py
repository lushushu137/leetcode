
def reverse(x):
    num = x
    res = []
    if x<0:
        num = -x
    while num:
        lastNum = num%10
        if lastNum != 0 or res !=[]:
            res.append(lastNum)
        num = num //10

    
    output = 0
    for i in range(len(res)):
        output += res[i]*(10**(len(res)-i-1))
    if abs(output) > 2**31:
        return 0
    if x<0:
        return -output
    else:
        return output

x = int(input())
print(reverse(x))