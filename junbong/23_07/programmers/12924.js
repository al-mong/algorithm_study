/**
누적합 배열을 만든다.
t를 항의 개수, k를 임의의 자연수라고 할 때
t를 1부터 늘려가면서
t * k + (0부터 t - 1까지의 누적합)이 n이 되는게 가능한지 확인한다.
즉, k = (n - 누적합) / t가 자연수인지 확인한다.
예를 들어, t = 3(항의 개수가 3)이라면, k + k + 1 + k + 2 = 3k + (0 + 1 + 2)
3k + 3 = 15에서 k = 4로 나눠떨어진다. 위 항에 대입하면 4 + 5 + 6으로 15가 된다.
**/

function solution(n) {
  if (n <= 2) {
    return 1;
  }

  let answer = 0;

  const cumul = [0];
  for (i = 1; i <= n; i++) {
    cumul.push(cumul[cumul.length - 1] + i);
  }

  for (t = 1; t < n; t++) {
    // k가 0 이하가 되는 경우
    if (cumul[t - 1] >= n) {
      break;
    }

    if ((n - cumul[t - 1]) % t === 0) {
      answer += 1;
    }
  }

  return answer;
}

console.log(solution(15));
