// A가 B보다 항상 크다는 가정이 없음 = 그냥 바꿔주는 게 좋을듯?

class Solution {
	public int solution(int n, int a, int b) {
		int answer = 0;
		int new_a = Math.min(a, b);
		int new_b = Math.max(a, b);
		while (true) {
			answer += 1;
			if (new_a % 2 == 1 && new_b == new_a + 1) {
				break;
			}
			new_a = (int) Math.ceil((double) new_a / 2);
			new_b = (int) Math.ceil((double) new_b / 2);
		}

		return answer;
	}
}