let itemList = [
  {
    value: 5,
    volume: 2,
  },
  {
    value: 2,
    volume: 4,
  },
  {
    value: 4,
    volume: 1,
  },
  {
    value: 8,
    volume: 4,
  },
];

function solveBag(itemList, bagVolume) {
  let dp = [];
  for (let i = 0; i < itemList.length + 1; i++) {
    let row = [];
    for (let j = 0; j < bagVolume + 1; j++) {
      if (i == 0) {
        row.push(0);
      } else if (j == 0) {
        row.push(0);
      } else {
        row.push(null);
      }
    }
    dp.push(row);
  }
  for (let i = 1; i < itemList.length + 1; i++) {
    for (let j = 1; j < bagVolume + 1; j++) {
      let currItem = itemList[i - 1];
      let notChoose = dp[i - 1][j];
      let choose =
        j >= currItem.volume
          ? currItem.value + dp[i - 1][j - currItem.volume]
          : 0;
      dp[i][j] = notChoose > choose ? notChoose : choose;
    }
  }
  return dp;
}

console.log(solveBag(itemList, 5));
