import java.util.*;

class Solution {
    public int solution(String[] user_id, String[] banned_id) {
        /** 
         * *을 제외한 모든 문자가 같은 후보군들을 딕셔너리<리스트>로 저장 (key = *rodo, value = [frodo, prodo])
         */
        Map<String, List<String>> candidate = new HashMap<>();
		for (String banUser: banned_id) {
			candidate.put(banUser, new ArrayList<>());
			for (String user: user_id) {
				if (banUser.length() == user.length()) {
					int idLength = banUser.length();
					boolean equals = true;
					for (int i = 0; i < idLength; i++) {
						if (!String.valueOf(banUser.charAt(i)).equals("*") && !String.valueOf(banUser.charAt(i)).equals(String.valueOf(user.charAt(i)))) {
							equals = false;
							break;
						}
					}
					if (equals) {
						candidate.get(banUser).add(user);
					}
				}
			}
		}

        /**
         * 정답 set 찾기
         */
		Set<Set<String>> answerList = new HashSet<>();
		findAllCombination(answerList, candidate, banned_id, new HashSet<>(), 0, banned_id.length);

		return answerList.size();
	}


	private void findAllCombination(Set<Set<String>> answerList, Map<String, List<String>> candidate, String[] banned_id, Set<String> set, int i, int n) {
		// 인덱스가 n 에 도착한다면 정답을 +1
        if (i == n) {
            answerList.add(new HashSet<>(set));

        // 인덱스가 n 이 아니라면 i를 증가시키며 재귀를 하지만
		} else {
			for (String id: candidate.get(banned_id[i])) {
				if (!set.contains(id)) {    // 중복요소가 있다면 가지치기
					set.add(id);            // 없다면 임시 set에 추가하고 재귀
					findAllCombination(answerList, candidate, banned_id, set, i+1, n);
					set.remove(id);         // 재귀를 마치고 돌아오면 임시 set에서 제거하고 for문 계속 돌기
				}
			}
		}
	}
}