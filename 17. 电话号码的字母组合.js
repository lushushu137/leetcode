var letterCombinations = function(digits) {
    if (digits === '') {
        return []
    }
    const map = {
        2: ['a','b','c'],
        3: ['d','e','f'],
        4: ['g','h','i'],
        5: ['j','k','l'],
        6: ['m', 'n', 'o'],
        7: ['p','q','r','s'],
        8: ['t','u','v'],
        9: ['w','x','y','z']
    };
    let lettersList = [];
    for (let i = 0; i < digits.length; i++) {
        lettersList.push(map[digits[i]]);
    };
    const func = (lettersList) => {
        if (lettersList.length === 1) {
            return lettersList[0];
        };
        let current = lettersList[0];
        let next = lettersList.slice(1);
        let subRes = func(next);
        let currentRes = []
        for (let j = 0; j < current.length; j++) {
            for (let k = 0; k < subRes.length; k++){
                currentRes.push(current[j]+ subRes[k]);
            }
        };
        // console.log(currentRes)
        return currentRes
    
    };
    return func(lettersList);
};

console.log(letterCombinations('234'));