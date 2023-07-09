function countOne(n) {
  return n.toString(2).split("1").length - 1;
}

function solution(n) {
  const oneCount = countOne(n);

  let next = n;
  let i = 1;

  while (true) {
    if (countOne(next + i) === oneCount) {
      return next + i;
    }
    i += 1;
  }
}

console.log(solution(15));
