/**
1. n을 반으로 나눠서 각각 어느 쪽에 있는지 판단
2. 서로 다른 쪽에 있다면, 반으로 나눈 범위의 길이를 2를 밑으로하는 로그 함수에 넣고, 반환 값 + 1을 return
3. 같은 쪽에 있다면 다시 1번부터 반복
**/

const solution = (n, a, b) => {
  if (a > b) {
    [a, b] = [b, a];
  }

  while (true) {
    n /= 2;

    if (a <= n && b > n) {
      return Math.log2(n) + 1;
    } else if (a > n && b > n) {
      // 둘 다 기준선 오른 쪽에 있는 경우 왼쪽으로 이동
      a -= n;
      b -= n;
    }
  }
};
