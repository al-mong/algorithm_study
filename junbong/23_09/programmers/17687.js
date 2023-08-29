/*
1. 최대 t * m 글자까지 말해야하는 숫자들을 저장해놓는다. ex) 5진법: 1234101112131420
2. answer의 길이가 t가 될 때까지 저장해놓은 숫자의
   j (j는 0부터 t - 1까지의 인덱스) * m + p 번째의 글자를 추가한다.
*/

function solution(n, t, m, p) {
  let answer = "";
  let toTell = "";
  let i = 0;

  while (toTell.length < t * m) {
    toTell += i.toString(n);
    i += 1;
  }

  for (let j = 0; j < t; j++) {
    answer += toTell.charAt(j * m + p - 1).toUpperCase();
  }

  return answer;
}
