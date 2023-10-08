function solution(A, B) {
  let answer = 0;
  let BIndex = 0;

  A.sort((a, b) => b - a);
  B.sort((a, b) => b - a);

  for (let AIndex = 0; AIndex < A.length; AIndex++) {
    if (A[AIndex] < B[BIndex]) {
      BIndex += 1;
      answer += 1;
    }
  }

  return answer;
}
