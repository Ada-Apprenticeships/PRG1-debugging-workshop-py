function findClosingParenthesis(str, openPos) {
  if (str[openPos] !== "(") {
    return -1;
  }

  let count = 0;
  let i = openPos;

  while (i < str.length) {
    if (str[i] === "(") {
      count++;
    } else if (str[i] === ")") {
      count--;
    }

    if (count === 0) {
      return i;
    }

    i++;
  }

  return -1;
}

console.log(findClosingParenthesis("Hello, (world). (Something Else).", 2)); // should return 31
