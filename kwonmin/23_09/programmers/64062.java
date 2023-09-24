// 생각 전개부터 하자
// 몇 명 까지 가능한지
// 범위 : 200000000 이네요
// 이분탐색으로 가능할듯?
// 2억이니껜,,, 헉
// 처음에 max를 잡을지 2만을 잡을 지 고민.
// max = n이 드니껜. 그래도 최초 범위를 줄이는 게 더 낫지 않을까?


public class Niniz {

	public int solution(int[] stones, int k) {

		int start = 1;
		int end = 200000000;

		while(start <= end){
			int mid = (start+end)/2;
			boolean flag = false;
			int empty = 0;

			for (int i = 0; i < stones.length; i++) {
				int stone = stones[i] - mid;
				if (stone <= 0) {
					empty++;
					if (empty >= k) {
						flag = true;
						break;
					}
				} else {
					empty = 0;
				}
			}
			if(flag) end = mid-1;
			else start = mid+1;

		}


		return start-1;
	}
}
