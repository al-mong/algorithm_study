// A가 B보다 항상 크다는 가정이 없음 = 그냥 바꿔주는 게 좋을듯?

class 예상대진표
{
	public int solution(int n, int a, int b)
	{
		int answer = 0;
		int new_a = Math.min(a,b);
		int new_b = Math.max(a,b);
		while(true){
			answer+=1;
			if (a%2 == 1 && b == a+1){
				break;
			}
			a = (int)Math.ceil((double)a/2);
			b = (int)Math.ceil((double)b/2);
		}

		return answer;
	}
}