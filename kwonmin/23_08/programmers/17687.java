public class Ngame {
	public String solution(int n, int t, int m, int p) {
		StringBuilder sb = new StringBuilder(); // 숫자 담아둘 스트링빌더
		int num = 0;
		while (sb.length() < (m*t)){    // 사람수 * 구해야하는 수만큼 구해놓기
			sb.append(Integer.toString(num++, n)); // 숫자를 n진수로 변환해서 넣기
		}
		StringBuilder answer = new StringBuilder(); // 정답을 담을 answer
		for (int i = 0; i < t; i++) {   // 순회하면서 튜브가 담을 순서의 인덱스 넣기
			answer.append(sb.charAt((p-1)+(m*i)));
		}

		return answer.toString().toUpperCase(); // 대문자로 변환해서 반환
	}
}
