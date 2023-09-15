import java.util.*;

public class Solution {
	public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {

		Map<String, Integer> revenue = new HashMap<>();
		Map<String, String> parent = new HashMap<>();

		// 수익 딕셔너리 초기화
		for (String s: enroll) {
			revenue.put(s, 0);
		}

		// 부모(추천인) 초기화
		for (int i = 0; i < enroll.length; i++) {
			parent.put(enroll[i], referral[i]);
		}

		// 판매금액이 생길 시 수익을 update 하는 함수 호출
		for (int i = 0; i < seller.length; i++) {
			updateRevenue(seller[i], amount[i] * 100, revenue, parent);
		}


		// enroll의 등록 순서대로 수익을 정리
		int[] answer = new int[enroll.length];
		for(int i = 0; i < enroll.length; i++) {
			answer[i] = revenue.get(enroll[i]);
		}

		return answer;
	}


	private void updateRevenue(String child, int amount, Map<String, Integer> revenue, Map<String, String> parent) {
		int childRevenue = revenue.get(child); // 현재 금액 
		int passMoney = amount / 10; // 부모에게 줄 금액
		// 현재 금액 업데이트 
		revenue.put(child, childRevenue + amount - passMoney); 
		// 부모가 - 가 아니고, 부모에게 줘야할 돈이 있을 때 재귀
		if (!Objects.equals(parent.get(child), "-") && passMoney != 0) {    
			updateRevenue(parent.get(child), passMoney, revenue, parent);
		}
	}


	public static void main(String[] args) {
		Solution s = new Solution();
		System.out.println(Arrays.toString(
			s.solution(new String[] { "john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young" }, new String[] { "-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward" },
				new String[] { "young", "john", "tod", "emily", "mary" }, new int[] { 12, 4, 2, 5, 10 })));
	}
}