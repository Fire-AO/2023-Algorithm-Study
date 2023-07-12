pattern = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']  # 패턴 배열로 나열

s = input()  # 문자열 입력

# 패턴을 하나씩 확인
for i in range(len(pattern)):
    if s.find(pattern[i]) != -1:  # 해당하는 패턴에 맞는 문자열 발견시 진행
        s = s.replace(pattern[i], '*')  # 발견시 해당 문자열을 * 변경

print(len(s))  # 결과 출력