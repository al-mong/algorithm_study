import java.util.*;

class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        ArrayList<Integer> answerList = new ArrayList();

        // 약관기간 해시맵 제작
        HashMap<Character, Integer> map = new HashMap<>();
        for (String term:terms) {
            char type = term.charAt(0);
            int check = Integer.parseInt(term.substring(2));
            map.put(type, check);
        }

        int today_year = Integer.parseInt(today.substring(0, 4));
        int today_month = Integer.parseInt(today.substring(5, 7));
        int today_day = Integer.parseInt(today.substring(8, 10));


        // 돌면서 확인
        for (int i=0; i < privacies.length; i++) {
            int year = Integer.parseInt(privacies[i].substring(0, 4));
            int month = Integer.parseInt(privacies[i].substring(5, 7));
            int day = Integer.parseInt(privacies[i].substring(8, 10));
            char type = privacies[i].charAt(11);

            day = day - 1;
            if (day == 0) {
                day = 28;
                month = month - 1;
                if (month == 0) {
                    month = 12;
                    year = year - 1;
                }
            }

            month = month + map.get(type);
            while (month > 12) {
                month = month - 12;
                year = year + 1;
            }


            // System.out.println(today_year);
            // System.out.println(year);
            // System.out.println(today_month);
            // System.out.println(month);
            // System.out.println(today_day);
            // System.out.println(day);


            // 오늘이 기준일보다 크면 배열에 담기
            if (today_year > year) {
                answerList.add(i+1);
            }else if (today_year == year && today_month > month) {
                answerList.add(i+1);
            }else if (today_year == year && today_month == month && today_day > day){
                answerList.add(i+1);
            }

        }

        int[] answer = new int[answerList.size()];
        for (int i = 0; i < answerList.size(); i++) {
            answer[i] = answerList.get(i);
        }

        return answer;
    }
}