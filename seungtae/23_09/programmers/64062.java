// 시도 1
// 97점.. 뭔짓을 해도 효율성 13번만 시간초과
import java.util.*;
class Solution {
    public int solution(int[] stones, int k) {
        int answer = Integer.MAX_VALUE;
        if (stones.length == 1) {
            return stones[0];
        }
        int[] newStones = new int[stones.length + 1];
        newStones[0] = Integer.MAX_VALUE;
        for(int i = 0; i < stones.length; i++) {
            newStones[i+1] = stones[i];
        }
        
        int i = 0;
        while (i < newStones.length-k) {
            int count = 0;
            int maxValue = 0;
            for(int j = i+1; j < i+1+k; j++) {
                if (j <= newStones.length && newStones[j] <= newStones[i]) {
                    maxValue = Math.max(maxValue, newStones[j]);
                    count += 1;
                } else {
                    break;
                }
            }
            if (count == k) {
                answer = Math.min(answer, maxValue);
            }
            i++;
        }
        
        return answer;
    }
}

// 시도 2

import java.util.ArrayDeque;
import java.util.Deque;


class Solution {
	public int solution(int[] stones, int k) {
		int answer = Integer.MAX_VALUE;
		Deque<Integer> deque = new ArrayDeque<>();

		for (int i = 0; i < stones.length; i++) {
			// #1. 새로운값이 추가될때 무조건 내림차순이 되도록 원소를 빼고 들어감
			while (!deque.isEmpty() && deque.peekLast() < stones[i]) {
				deque.removeLast();
			}
			deque.add(stones[i]);

			// 정답은 k-1칸 이상 건너갔을때부터 계산하면 된다
			if (i >= k - 1) {
				 // #1. 때문에 deque의 첫번째는 항상 가장 큰 값이다
				answer = Math.min(answer, deque.getFirst());

				 // #1. 때문에 deque에 인덱스가 듬성듬성 들어갈 수도 있기때문에 
				 // deque의 첫번째 요소가 for문을 도는 i 보다 징검다리만큼 인덱스 차이나면 빼주기
				if (deque.getFirst() == stones[i - k + 1]) {
					deque.removeFirst();
				}
			}
		}

		return answer;
	}



	public static void main(String[] args) {
		Solution s = new Solution();
		s.solution(new int[] {7, 6, 5, 3, 2, 1, 4, 2, 5, 1}, 3);
//		s.solution(new int[] {10, 0, 0, 0, 7, 0 ,0}, 3);
//		s.solution(new int[] {2, 5, 10, 12, 2, 8, 100, 100, 100}, 3);
	}
}
