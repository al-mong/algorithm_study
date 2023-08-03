// 강의실 문제 비스무레
// 최소값만 넣으면 안되고, 무게 제한을 고려해서...
// 근데 투 포인터로 풀면 어떨까 라는 생각

import java.util.Arrays;

public class BoatEscape {

	public static void main(String[] args) {
		Solution sol = new Solution();
		int[] input = {70,80,50};
		System.out.println(sol.solution(input, 100));
	}
}

class Solution {
	public int solution(int[] people, int limit) {
		int answer = 0;
		Arrays.sort(people);    // 가벼운 순으로 정렬
		int start = 0;          // 투포인터 시작
		int end = people.length-1;  // 투포인터 끝
		while(start<=end){  // 앞지를때까지
			if(people[start]+people[end] > limit){  // 둘을 못태울 경우 = 무거운 놈 하나만 태워 보냄
				end--;
			} else if (start == end) {  // 같을 경우 == 한명만 남았다는 뜻이므로 태워보냄
				end--;
			} else {    // 둘 다 태울 수 있으면, 둘 다 태워보냄
				start++;
				end--;
			}
			answer++;
		}

		return answer;
	}
}