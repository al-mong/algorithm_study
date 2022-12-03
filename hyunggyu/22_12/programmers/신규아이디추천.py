def solution(new_id): # 대입
    # 1. 대문자 -> 소문자
    new_id = new_id.lower()
    # 2. 소문자, 숫자, 빼기, 밑줄, 마침표 제외 제거
    renew_id = ''
    zero = 48
    nine = 57
    alpa_a = 97
    alpa_z = 122
    doubledot = True # 제일 처음 dot 제거
    for i in new_id:
        # 0~9 : 48~57
        # a~z : 97~122
        if doubledot == False and i == '.':
            renew_id = renew_id + i
            doubledot = True
        elif i == '_':
            renew_id = renew_id + i
            doubledot = False
        elif i == '-':
            renew_id = renew_id + i
            doubledot = False
        elif zero <= ord(i) <= nine:
            renew_id = renew_id + i
            doubledot = False
        elif alpa_a <= ord(i) <= alpa_z:
            renew_id = renew_id + i
            doubledot = False
    # 3. .이 2개 이상 -> . 1개
    # 4. .이 시작 또는 끝일 경우 제거
    if renew_id != '' and renew_id[-1] == '.':
        renew_id = renew_id[:-1]
    # 5. ''빈문자열 이면 "a" 대입
    word_length = len(renew_id)
    if word_length == 0:
        renew_id = 'aaa'
    # 6. 16자 이상이면 앞 15개만 놔두기 + 마지막 . 이면 제거
    elif word_length > 15:
        renew_id = renew_id[:15]
        if renew_id[-1] == '.':
            renew_id = renew_id[:-1]
    # 7. 2자 이하이면 마지막 문자 반복 -> 3글자가 될때까지 -> '.' 이면?
    elif word_length == 1:
        renew_id = renew_id*3
    elif word_length == 2:
        renew_id = renew_id + renew_id[1]
    answer = renew_id
    return answer