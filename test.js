let tryWhileReturn = function (a) {
  while (a > 0) {
    if (a < 5) {
      return a;
    }
    a--;
  }
  return a;
};
console.log(tryWhileReturn(10));
