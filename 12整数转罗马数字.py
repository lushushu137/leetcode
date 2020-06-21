def intToRoman(num):
    digits = [
        'I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M'
    ]
    keys = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

    res = ''
    while num > 0:
        digit = keys.pop()
        char = digits.pop()
        # print(digit, num)
        while num >= digit:
            res += char
            num -= digit

    return res


print(intToRoman(1994))
