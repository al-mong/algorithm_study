def solution(new_id):
    # 1,2 단계
    index = 0  # 현재 위치의 문자열을 나타내주는 인덱스 변수 선언
    while index < len(new_id):

        # 대문자면 소문자로 바꾸고 다음 문자열 검사하러 가기
        if 65 <= ord(new_id[index]) <= 90:
            new_id = new_id.replace(new_id[index], chr(ord(new_id[index])+32))
            index += 1
            continue

        # 유효한 문자열이면 다음 문자열 검사하러 가기
        if new_id[index] == '.' or new_id[index] =='-' or new_id[index] == '_' or 97 <= ord(new_id[index]) <= 122 or 48 <= ord(new_id[index]) <= 57:
            index += 1
            continue

        # 유효하지 않은 문자열이면 삭제하고 (길이가 줄어들었으니) 그자리 다시 검사하게 index 증가시키지 않기
        new_id = new_id.replace(new_id[index], '')

    # 3 단계 - ".." 이 없을때까지 대체하기
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    # 4 단계 - 길이가 0인걸 고려하지 않았을 땐 인덱스에러가 나서 같이 검사함!
    if len(new_id) != 0 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) != 0 and new_id[-1] == '.':
        new_id = new_id[:-1]

    # 5 단계 - 비어있을땐 a 를 채우기
    if new_id == '':
        new_id = 'a'

    # 6 단계 - 15자로 자르고 끝 . 지우기
    new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]

    # 7 단계 - 길이가 2이하면 증가시키기 
    while len(new_id) < 3:
        new_id += new_id[-1]

    answer = new_id
    return answer

if __name__ == '__main__':
    print(solution("...!@BaT#*..y.abcdefghijklm"))
    print(solution("z-+.^."))
    print(solution("=.="))
    print(solution("123_.def"))
    print(solution("abcdefghijklmn.p"))
