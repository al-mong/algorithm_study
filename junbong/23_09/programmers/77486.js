function solution(enroll, referral, seller, amount) {
  const answer = new Array(enroll.length).fill(0);
  const index = {}; // 이름에 대한 인덱스
  const recommenders = {}; // 구성원의 추천인

  // index, recommenders 채우기
  for (let i = 0; i < enroll.length; i++) {
    index[enroll[i]] = i;
    recommenders[enroll[i]] = referral[i];
  }

  // answer 채우기
  for (let j = 0; j < seller.length; j++) {
    // seller[j]의 이익 계산
    answer[index[seller[j]]] += Math.ceil(amount[j] * 100 * 0.9);
    // seller[j]의 추천인
    let recommender = recommenders[seller[j]];
    // seller[j]의 추천인들에게 갈 이익금
    let distribution = Math.floor(amount[j] * 100 * 0.1);

    while (distribution > 0 && recommender !== "-") {
      // 추천인에게 이익 분배
      answer[index[recommender]] += Math.ceil(distribution * 0.9);
      // 추천인의 추천인
      recommender = recommenders[recommender];
      // 추천인의 추천인들에게 갈 이익금
      distribution = Math.floor(distribution * 0.1);
    }
  }

  return answer;
}
