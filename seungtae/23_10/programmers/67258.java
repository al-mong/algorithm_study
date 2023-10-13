package programmers.gems;

import java.util.*;

class Solution {
	public int[] solution(String[] gems) {
		int[] answer = new int[] {1, gems.length};

		// 보석: 0 으로 모든 Map을 초기화
		Map<String, Integer> gemMap = new HashMap<>();
		for (String gem: gems) {
			gemMap.put(gem, 0);
		}

		Set<String> gemSet = new HashSet<>();
		int count = gemMap.keySet().size();
		int left = 0;
		int right = 0;

		while (true) {
			boolean flag = gemSet.size() == count;

			if (flag) {
				gemMap.put(gems[left], gemMap.get(gems[left])-1); // 현재 가능한 상황일 때 left 보석을 줄임
				if (gemMap.get(gems[left]) == 0) {      // left 보석 개수가 0이 되면
					gemSet.remove(gems[left]);          // Set 에서 제거
				}
				left += 1;

				if (right - left < answer[1] - answer[0]) { // 정답이 더 짧으면 갱신
					answer[0] = left;
					answer[1] = right;
				}
			} else {
				if (right == gems.length) { // 현재 불가능한 상황일 때 더 추가할 게 없으면 종료
					break;
				}

				gemSet.add(gems[right]);                            // right 보석을 Set에 추가
				gemMap.put(gems[right], gemMap.get(gems[right])+1); // right 보석 개수를 +1
				right += 1;
			}
		}
		return answer;
	}


	public static void main(String[] args) {
		Solution s = new Solution();
		System.out.println(Arrays.toString(s.solution(new String[] { "ZZZ", "YYY", "NNNN", "YYY", "BBB" })));
	}
}