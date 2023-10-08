function isCandidate(userIdItem, bannedIdItem) {
  if (userIdItem.length === bannedIdItem.length) {
    for (let i = 0; i < userIdItem.length; i++) {
      if (bannedIdItem[i] !== "*" && userIdItem[i] !== bannedIdItem[i]) {
        return false;
      }
    }
    return true;
  }
  return false;
}

function solution(userId, bannedId) {
  let answer = new Set();
  const userCheck = new Array(userId.length).fill(0);

  function dfs(j, candidates) {
    if (j === bannedId.length) {
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
