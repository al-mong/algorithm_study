function solution(msg) {
  const answer = [];
  const dict = {}; // 사전
  let regiNum = 27; // 등록 번호

  while (msg.length >= 2) {
    // 남은 글자가 사전에 있다면 색인 번호 출력하고 break
    if (dict.hasOwnProperty(msg)) {
      answer.push(dict[msg]);
      break;
    }

    // i: w 길이
    for (i = 1; i <= msg.length - 1; i++) {
      const w = msg.substring(0, i);
      const c = msg.charAt(i);

      // w + c가 사전에 없다 <-> 현재 w가 일치하는 가장 긴 문자열이다
      if (!dict.hasOwnProperty(w + c)) {
        // 길이 1이면 사전 없이 아스키코드 이용
        if (w.length === 1) {
          answer.push(w.charCodeAt(0) - 64);
        } else {
          answer.push(dict[w]);
        }

        // msg에서 w 제거
        msg = msg.substring(i);

        // 사전 등록
        dict[w + c] = regiNum;
        regiNum += 1;

        break;
      }
    }
  }

  // 한 글자 남은 경우
  if (msg.length === 1) {
    answer.push(msg.charCodeAt(0) - 64);
  }

  return answer;
}
