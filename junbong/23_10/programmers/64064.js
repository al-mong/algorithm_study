// 아이디가 불량 사용자 후보가 될 수 있는지 판단
function isCandidate(userIdItem, bannedIdItem) {
  if (userIdItem.length === bannedIdItem.length) {
    const regexPattern = new RegExp(`^${bannedIdItem.replace(/\*/g, ".*")}$`);
    return regexPattern.test(userIdItem);
  }
}

function solution(userId, bannedId) {
  let answer = new Set();
  const userCheck = new Array(userId.length).fill(0);

  function dfs(j, candidates) {
    if (j === bannedId.length) {
      // 문자열 정렬해서 추가, 023과 203은 같은 것이므로
      answer.add(candidates.split("").sort().join(""));
      return;
    }

    for (let i = 0; i < userId.length; i++) {
      if (
        !userCheck[i] &&
        j < bannedId.length &&
        isCandidate(userId[i], bannedId[j])
      ) {
        userCheck[i] = 1;
        candidates += new String(i);

        dfs(j + 1, candidates);

        userCheck[i] = 0;
        candidates = candidates.substring(0, candidates.length - 1);
      }
    }
  }

  dfs(0, "");

  return answer.size;
}
