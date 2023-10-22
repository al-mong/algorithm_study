function solution(board) {
  const dx = [0, 0, 1, -1];
  const dy = [1, -1, 0, 0];
  const queue = [[0, 0, 0, undefined]];
  const N = board.length;
  const costArray = new Array(N);
  for (let i = 0; i < N; i++) {
    costArray[i] = new Array(N);
    for (let j = 0; j < N; j++) {
      costArray[i][j] = new Array(4).fill(0);
    }
  }

  while (queue.length > 0) {
    const cur = queue.shift();
    const row = cur[0],
      col = cur[1],
      cost = cur[2],
      lastDir = cur[3];

    for (let i = 0; i <= 3; i++) {
      const nr = row + dx[i],
        nc = col + dy[i];

      if (nr < 0 || nr >= N || nc < 0 || nc >= N || board[nr][nc] === 1)
        continue;

      let newCost;

      if (lastDir !== undefined && lastDir !== i) {
        newCost = cost + 600;
      } else {
        newCost = cost + 100;
      }

      if (!costArray[nr][nc][i] || newCost < costArray[nr][nc][i]) {
        costArray[nr][nc][i] = newCost;
        queue.push([nr, nc, newCost, i]);
      }
    }
  }

  let answer = N * N * 600;

  for (const answerCand of costArray[N - 1][N - 1]) {
    if (answerCand === 0) continue;

    answer = answerCand < answer ? answerCand : answer;
  }

  return answer;
}
