document = input() # 문서 입력
sWord = input() # 검색어

index=0 # 인덱스

result=-1 # 결과 값

while index!=-1:
    index=document.find(sWord) # 문서에서 검색어가 있는 지 찾는다 있다면 첫번째 인덱스를 반환 없다면 -1을 반환
    if index!=0: # 검색어가 첫번째에 존재하지 않는다면 진행
        document=document[index:] # 문서에서 찾은 검색어의 인덱스 전에 있는 문자들을 제거
    document=document.replace(  sWord,'',1) # 검색어를 제거
    result+=1 # 결과값 1증가

print(result) # 결과 출력
