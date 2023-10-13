// 0부터 시작해서 start, end 가장 큰 범위를 찾기
// 무조건 해당 밸류가 들어있을 경우에만 start 늘리기
// 해당 밸류가 몇 개 들어있는지는... map 쓰는 게 맞지 않나??

import java.util.HashMap;
import java.util.HashSet;


public class Gems {
	// Set으로 체크한 버전
	// 근데 ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"] 를 통과 못함
	// 뭐랄까 마지막 거랑 첫번째 것만 비교하니까
	// 당기기가 안되나 봄
	// Set말고 Map으로 하면 될 것 같음
	public int[] solution1(String[] gems) {
		HashSet<String> gemSet = new HashSet<>();
		// 약간 while 로 현재 gem이랑 같으면 여러 번 start 올리기
		int start = 0;
		int x = 0;
		int y = 0;
		for (int i = 0; i < gems.length; i++) {
			if(!gemSet.contains(gems[i])){
				gemSet.add(gems[i]);
				x = start;
				y = i;
				continue;
			}
		while(gems[start].equals(gems[i]) && start != i){
			start++;
			if(i-start < y-x){
				x = start;
				y = i;
			}
		}

		}
		return new int[]{x+1,y+1};
	}

	// Map으로 바꾸니 해결. 마지막과 같을 때만 세는 게 아니라, 시작이 2 이상일 경우 한칸 더 전진하도록 수정
	public int[] solution2(String[] gems) {
		HashMap<String, Integer> gemMap = new HashMap<>();

		int start = 0;
		int x = 0;
		int y = 0;
		for (int i = 0; i < gems.length; i++) {
			if(!gemMap.containsKey(gems[i])){
				gemMap.put(gems[i], 1);
				x = start;
				y = i;
				continue;
			}
			gemMap.put(gems[i], gemMap.get(gems[i])+1);
			while(gemMap.get(gems[start]) > 1 && start != i){
				gemMap.put(gems[start], gemMap.get(gems[start])-1);
				start++;
				if(i-start < y-x){
					x = start;
					y = i;
				}
			}

		}
		return new int[]{x+1,y+1};
	}
}
