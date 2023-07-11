/**
카펫의 가로 길이가 세로 길이보다 같거나 길다는 것을 고려하면서
1. 노란색의 가로 * 세로가 노란색의 개수가 되는 것을 만족하는지 확인한다.
2. 위 조건에 맞는 필요한 갈색 테두리 개수가 주어진 brown과 같은지 확인한다.
3. 테두리 1줄 감싸져 있으니 [노란색의 가로 + 2, 노란색의 세로 + 2] 출력한다.
**/

function solution(brown, yellow) {
  // 세로 길이(ver)는 노란색 타일의 제곱근까지만 보면 됨
  for (ver = 1; ver <= Math.sqrt(yellow); ver++) {
    if (yellow % ver === 0) {
      const hor = yellow / ver;
      const requiredBrown = (hor + ver) * 2 + 4;

      if (brown === requiredBrown) {
        return [hor + 2, ver + 2];
      }
    }
  }
}
